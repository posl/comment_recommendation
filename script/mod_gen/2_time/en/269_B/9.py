def main():
    # read the input
    table = []
    for _ in range(10):
        table.append(input())
    # find the answer
    for i in range(10):
        if table[i] == ".........#":
            A = i + 1
    for i in range(10):
        if table[i] == "..........":
            B = i
    for i in range(10):
        if table[0][i] == "#":
            C = i + 1
    for i in range(10):
        if table[0][i] == ".":
            D = i
    # print the answer
    print(A, B)
    print(C, D)

if __name__ == '__main__':
    main()