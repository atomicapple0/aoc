with open("02-rps") as f:
    raw = f.read()

lookup = {
    ("A", "X"): 0 + 3,
    ("A", "Y"): 3 + 1,
    ("A", "Z"): 6 + 2,
    ("B", "X"): 0 + 1,
    ("B", "Y"): 3 + 2,
    ("B", "Z"): 6 + 3,
    ("C", "X"): 0 + 2,
    ("C", "Y"): 3 + 3,
    ("C", "Z"): 6 + 1,
}

rounds = [line.split(" ") for line in raw.split("\n")]

score = 0
for a,x in rounds:
    score += lookup[(a,x)]

print(score)