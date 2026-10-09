def knightAdjacent (r c s d : Nat) : Prop :=
  ((r + 1 = s \/ s + 1 = r) /\ (c + 2 = d \/ d + 2 = c)) \/
  ((r + 2 = s \/ s + 2 = r) /\ (c + 1 = d \/ d + 1 = c))

theorem knightAdjacent_symm {r c s d : Nat}
    (h : knightAdjacent r c s d) :
    knightAdjacent s d r c := by
  rcases h with h | h
  · rcases h with ⟨hr, hc⟩
    left
    constructor
    · rcases hr with hr | hr
      · right
        exact hr
      · left
        exact hr
    · rcases hc with hc | hc
      · right
        exact hc
      · left
        exact hc
  · rcases h with ⟨hr, hc⟩
    right
    constructor
    · rcases hr with hr | hr
      · right
        exact hr
      · left
        exact hr
    · rcases hc with hc | hc
      · right
        exact hc
      · left
        exact hc
