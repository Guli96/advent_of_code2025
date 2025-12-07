def get_coordinate(x, y, lines):
    if x < 0 or y < 0:
        return False
    if y >= len(lines):
        return False
    if x >= len(lines[y]):
        return False
    return lines[x][y] == '@'

def get_adjacent_roll_count(x, y, lines):
    output = 0
    for x_iter in range(-1, 2):
        for y_iter in range(-1, 2):
            if y_iter == x_iter == 0:
                continue
            if get_coordinate(x + x_iter, y + y_iter, lines):
                output += 1
    return output

def part1(lines):
    output = 0
    for x in range(0, len(lines)):
        for y in range(0, len(lines[x])):
            if get_coordinate(x, y, lines) and get_adjacent_roll_count(x, y, lines) < 4:
                print(x, y)
                output += 1
    return output

def print_lines(lines):
    for line in lines:
        print(line)
    print('-------------')

def part2(lines):
    lines_copy = lines.copy()
    output = 0
    removed_rolls = True
    while removed_rolls:
        removed_rolls = False
        for x in range(0, len(lines)):
            for y in range(0, len(lines[x])):
                if get_coordinate(x, y, lines) and get_adjacent_roll_count(x, y, lines) < 4:
                    #print(x, y)
                    removed_rolls = True
                    lines_copy[x] = lines_copy[x][:y] + '.' + lines_copy[x][y+1:]
                    output += 1
        lines = lines_copy
        print_lines(lines)
    return output
