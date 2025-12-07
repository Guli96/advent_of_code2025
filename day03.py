def get_bank_max_joltage(bank):
    max_tens_place = max(bank[:-1])
    max_tens_place_index = int(bank.index(max_tens_place))
    max_ones_place = max(bank[max_tens_place_index + 1:])

    max_joltage = int(max_tens_place + max_ones_place)
    return max_joltage

def remove_min_from_bank(bank):
    min_joltage = min(bank)
    min_joltage_index = bank.index(min_joltage)
    return bank[:min_joltage_index] + bank[min_joltage_index+1:]

def bank_window_max(bank, window_start, window_end = 4):
    bank_window = bank[window_start:window_start+window_end]
    output = max(bank_window)
    output_index = bank.index(output)
    return output_index

def get_bank_max_joltage_part2(bank):
    bank_copy = bank
    bank_output = ""
    window_start = 0

    while len(bank_output) < 12:
        remaining_bank = len(bank_copy)
        remaining_free_places = 12 - len(bank_output)
        window_end = remaining_bank - remaining_free_places + 1

        max_index = bank_window_max(bank_copy, window_start, window_end)
        bank_output += bank_copy[max_index]
        bank_copy = bank_copy[max_index+1:]

    return int(bank_output)

def part1(lines):
    joltage_sum = 0
    for bank in lines:
        joltage_sum += get_bank_max_joltage(bank)
    return(joltage_sum)

def part2(lines):
    joltage_sum = 0
    for bank in lines:
        joltage_sum += get_bank_max_joltage_part2(bank)
    return joltage_sum