def get_input_lines(day: int, demo = False):
    filepath = f"input\\{str(day).rjust(2, '0')}"

    if demo:
        filepath += "_d"
    file = open(filepath)
    output = file.read().splitlines()
    file.close()
    return output
