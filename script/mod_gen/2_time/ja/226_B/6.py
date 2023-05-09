def main():
    N = int(input())
    L = []
    for i in range(N):
        l = list(map(int, input().split()))
        L.append(l)
    L.sort()
    count = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()