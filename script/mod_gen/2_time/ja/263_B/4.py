def main():
    N = int(input())
    P = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        parent = P[i]
        while parent != 0:
            ans += 1
            parent = P[parent-1]
            if parent == 0:
                break
    print(ans)

if __name__ == '__main__':
    main()