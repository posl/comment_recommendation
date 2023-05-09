def main():
    N = int(input())
    c = input()
    count = 0
    r = 0
    w = 0
    for i in range(N):
        if c[i] == "R":
            r += 1
        else:
            w += 1
    for i in range(r):
        if c[i] == "W":
            count += 1
    print(count)

if __name__ == '__main__':
    main()