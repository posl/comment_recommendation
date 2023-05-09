def main():
    input_line = input()
    input_list = input_line.split()
    n, a, b = int(input_list[0]), int(input_list[1]), int(input_list[2])
    print(min(n * a, b))
