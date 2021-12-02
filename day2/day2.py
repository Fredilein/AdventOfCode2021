with open('input.txt') as f:
    cmds = f.readlines()
    cmds = [c.rstrip() for c in cmds]

def part1():
    fwd = 0
    depth = 0
    for c in cmds:
        (d, x) = c.split(" ")
        if d == "forward":
            fwd += int(x)
        elif d == "down":
            depth += int(x)
        elif d == "up":
            depth -= int(x)
    return fwd * depth

def part2():
    fwd = 0
    depth = 0
    aim = 0
    for c in cmds:
        (d, x) = c.split(" ")
        x = int(x)
        if d == "forward":
            fwd += x
            depth += aim * x
        elif d == "down":
            aim += x
        elif d == "up":
            aim -= x
    return fwd * depth


res = part1()
print("Star 1: ", res)

res = part2()
print("Star 2: ", res)
