with open('01-calorie') as f:
    raw = f.read()

elf = [sum([int(cal_str) for cal_str in cals_str.split('\n')]) for cals_str in raw.split('\n\n')]

a = max(elf)
elf.remove(a)
b = max(elf)
elf.remove(b)
c = max(elf)
elf.remove(c)
print(a+b+c)