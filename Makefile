.PHONY: test reproduce c-check sage-check lean-check clean

test:
	pytest

reproduce:
	bash scripts/reproduce.sh

c-check:
	cc -std=c11 -O2 -Wall -Wextra -Wpedantic c/verify_solution.c -o /tmp/verify_solution

sage-check:
	sage sage/verify_modular_family.sage

lean-check:
	cd lean && lake build

clean:
	rm -f results/*.csv results/*.json
