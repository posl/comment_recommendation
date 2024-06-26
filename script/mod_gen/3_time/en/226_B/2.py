def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    L.sort(key=lambda x: x[1:])
    cnt = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()