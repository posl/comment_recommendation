def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort(key=lambda x: x[0])
    #print(L)
    ans = 0
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans+1)

if __name__ == '__main__':
    main()