with open('input.txt') as f:
    depths = f.readlines()
    depths = [d.rstrip() for d in depths]

def part1():
    deeper_counter = 0
    for i in range(1, len(depths)):
        if int(depths[i]) > int(depths[i-1]):
            deeper_counter += 1

    print('Star 1: ', deeper_counter)

def part2():
    deeper_counter = 0
    last_depth = 9999999
    for i in range(2, len(depths)):
        curr_depth = int(depths[i]) + int(depths[i-1]) + int(depths[i-2])
        if curr_depth > last_depth:
            deeper_counter += 1
        last_depth = curr_depth

    print('Star 2: ', deeper_counter)

part1()
part2()
