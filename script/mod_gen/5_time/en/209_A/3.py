def main():
    input_line = input()
    input_line = input_line.split()
    a = int(input_line[0])
    b = int(input_line[1])
    if a > b:
        print(0)
    else:
        print(b - a + 1)
main()
