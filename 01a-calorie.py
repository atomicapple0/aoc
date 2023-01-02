with open('calorie') as f:
    raw = f.read()

elf = max([sum([int(cal_str) for cal_str in cals_str.split('\n')]) for cals_str in raw.split('\n\n')])

print(elf)