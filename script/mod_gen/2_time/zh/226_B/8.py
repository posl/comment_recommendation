def main():
    N = int(input())
    L = []
    for i in range(N):
        a = list(map(int, input().split()))
        L.append(a)
    result = 1
    for i in range(N):
        for j in range(i + 1, N):
            if L[i] == L[j]:
                break
            if j == N - 1:
                result += 1
    print(result)

if __name__ == '__main__':
    main()