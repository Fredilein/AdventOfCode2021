with open('input.txt') as f:
    bins = f.readlines()
    bins = [b.rstrip() for b in bins]

def part1():
    gamma = ''
    for p in range(len(bins[0])):
        ones = 0
        zeros = 0
        for b in bins:
            if b[p] == '1':
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += '1'
        else:
            gamma += '0'
    epsilon = ''
    for g in gamma:
        if g == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)

def filterstep(arr, i, strat='oxy'):
    ones = []
    zeros = []
    for a in arr:
        if a[i] == '1':
            ones.append(a)
        else:
            zeros.append(a)
    if strat == 'oxy':
        if len(ones) >= len(zeros):
            return ones
        return zeros
    else:
        if len(zeros) > len(ones):
            return ones
        return zeros

i = 0
arr = bins.copy()
while i < len(bins) and len(arr) > 1:
    arr = filterstep(arr, i, strat='oxy')
    i += 1

oxygen_rating = arr[0]

i = 0
arr = bins.copy()
while i < len(bins) and len(arr) > 1:
    arr = filterstep(arr, i, strat='scrubber')
    i += 1

scrubber_rating = arr[0]

res = part1()
print("Star 1: ", res)
print("Star 2: ", int(oxygen_rating, 2) * int(scrubber_rating, 2))
