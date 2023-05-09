def main():
    N = int(input())
    P = list(map(int, input().split()))
    c = 0
    min = 1000000
    for i in range(N):
        if P[i] < min:
            c += 1
            min = P[i]
    print(c)

if __name__ == '__main__':
    main()