def problem207_b():
    A, B, C, D = map(int, input().split())
    if A <= B*D:
        print(0)
        exit()
    count = 1
    while True:
        A += B
        A -= C
        if A <= B*D:
            print(count)
            exit()
        count += 1

if __name__ == '__main__':
    problem207_b()