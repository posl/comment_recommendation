def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0,0)
    ans = 0
    for i in range(1, N+1):
        if P[i] < i:
            ans += 1
        else:
            ans += 1
            j = P[i]
            while j < i:
                ans += 1
                j = P[j]
    print(ans)

if __name__ == '__main__':
    main()