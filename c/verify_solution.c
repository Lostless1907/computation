#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

static bool verify(int n, const int *p) {
    if (n < 1) return false;

    bool *cols = calloc((size_t)n, sizeof(bool));
    bool *down = calloc((size_t)(2 * n - 1), sizeof(bool));
    bool *up = calloc((size_t)(2 * n - 1), sizeof(bool));

    if (!cols || !down || !up) {
        free(cols);
        free(down);
        free(up);
        return false;
    }

    bool valid = true;

    for (int r = 0; r < n; ++r) {
        int c = p[r];
        if (c < 0 || c >= n) {
            valid = false;
            break;
        }

        int d = r - c + n - 1;
        int u = r + c;
        if (cols[c] || down[d] || up[u]) {
            valid = false;
            break;
        }
        cols[c] = down[d] = up[u] = true;
    }

    free(cols);
    free(down);
    free(up);
    if (!valid) return false;

    for (int r = 0; r < n; ++r) {
        for (int s = r + 1; s < n && s <= r + 2; ++s) {
            int dr = s - r;
            int dc = abs(p[s] - p[r]);
            if ((dr == 1 && dc == 2) || (dr == 2 && dc == 1))
                return false;
        }
    }
    return true;
}

int main(void) {
    int n;
    if (scanf("%d", &n) != 1 || n < 1 || n > 100000) return 2;

    int *p = malloc((size_t)n * sizeof(int));
    if (!p) return 2;

    for (int i = 0; i < n; ++i) {
        if (scanf("%d", &p[i]) != 1) {
            free(p);
            return 2;
        }
    }

    bool valid = verify(n, p);
    free(p);
    puts(valid ? "VALID" : "INVALID");
    return valid ? 0 : 1;
}
