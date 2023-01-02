with open("02-rps") as f:
    raw = f.read()

# strategy = {"A": "Y", "B": "X", "C": "Z"}
a2x = {"A": "X", "B": "Y", "C": "Z"}
x2a = {"X": "A", "Y": "B", "Z": "C"}
pts = {"A": 1, "B": 2, "C": 3}
beat = {"A": "B", "B": "C", "C": "A"}

rounds = [line.split(" ") for line in raw.split("\n")]

score = 0
for a,x in rounds:
    b = x2a[x]
    s = pts[b]
    if a == b:  # tie
        s += 3
    elif beat[a] == b:  # win
        s += 6
    else:  # lose
        s += 0
    score += s
    print(s)

print(score)