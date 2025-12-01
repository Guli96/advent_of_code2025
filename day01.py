import string

def rotate_dial(rot, dial):
    direction = rot[0]
    amount = int(rot.strip(string.ascii_letters))
    zeroes = 0
    dial_o = dial
    if direction == 'R':
        dial += amount
        if dial > 99:
            while dial > 99:
                zeroes += 1
                dial -= 100
    else:
        dial -= amount
        if dial < 0:
            while dial < 0:
                zeroes += 1
                dial += 100
        if dial == 0:
            zeroes += 1
        if dial_o == 0: # 0-ról kezdtük a visszalépést, szóval az első hátratekerést nem kell számolni
            zeroes -= 1
    return dial, zeroes

def part1(lines):
    dial_start = 50
    dial = dial_start
    zeroes = 0

    for line in lines:
        dial, foo = rotate_dial(line, dial)
        if dial == 0:
            zeroes+=1
        print(dial)
    return zeroes

def part2(lines):
    dial_start = 50
    dial = dial_start
    zeroes = 0
    for line in lines:
        dial, new_zeroes = rotate_dial(line, dial)
        zeroes += new_zeroes
    return zeroes