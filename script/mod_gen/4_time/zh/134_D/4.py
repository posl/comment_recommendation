def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0]*N
    for i in range(N):
        if a[i] == 1:
            b[i] = 1
            for j in range(2, N//i+1):
                b[i*j-1] += 1
    c = []
    for i in range(N):
        if b[i] % 2 != a[i]:
            c.append(i+1)
    if len(c) == 0:
        print(0)
    else:
        print(len(c))
        print(*c)

if __name__ == '__main__':
    main()