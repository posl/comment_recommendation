def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A = [x % 200 for x in A]
    D = {}
    for a in A:
        D[a] = D.get(a, 0) + 1
    ans = 0
    for k, v in D.items():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()