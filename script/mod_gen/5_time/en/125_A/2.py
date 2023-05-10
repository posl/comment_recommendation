def main():
    input_line = input()
    input_line = input_line.split()
    a = int(input_line[0])
    b = int(input_line[1])
    t = int(input_line[2])
    result = 0
    for i in range(1, t + 1):
        if i % a == 0:
            result += b
    print(result)

if __name__ == '__main__':
    main()