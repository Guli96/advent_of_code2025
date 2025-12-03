import re

def is_invalid(product_id):
    str_id = str(product_id)
    product_id_length = len(str_id)
    if product_id_length%2 != 0:
        return False

    half_product_id_length = int(product_id_length/2)
    first_part = str_id[0:half_product_id_length]
    second_part = str_id[half_product_id_length:]
    if second_part[0] == '0':
        return False
    return first_part == second_part

def is_invalid_p2(product_id):
    str_id = str(product_id)
    product_id_length = len(str_id)

    return re.search(r"^(.*)\1+$", str_id) is not None

    half_product_id_length = int(product_id_length/2)

    for i in range(1, half_product_id_length+1):
        if product_id_length % i != 0:
            continue
        pattern_to_match = str_id[0:i]
        regex_pattern = "^(.{"+str(i)+r"}).*\1$"
        x = re.search(regex_pattern, str_id)
        if x is not None:
            print(str_id)
            return True
    return False

def get_ranges(lines):
    split_ranges = lines[0].split(',')
    output = []
    for spl in split_ranges:
        nums = spl.split('-')
        output.append((int(nums[0]), int(nums[1])))
    return output

def part1(lines):
    total = 0
    ranges = get_ranges(lines)
    for num_pair in ranges:
        for i in range(num_pair[0], num_pair[1]+1):
            if is_invalid(i):
                total += i
                print(i)
    print(total)

def part2(lines):
    total = 0
    ranges = get_ranges(lines)
    for num_pair in ranges:
        for i in range(num_pair[0], num_pair[1]+1):
            if is_invalid_p2(i):
                total += i
                print(i)
    print(total)


