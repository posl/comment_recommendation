def main():
    N = int(input())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    n = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            n += 1
    print(n)

if __name__ == '__main__':
    main()