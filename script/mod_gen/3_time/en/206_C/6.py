def main():
    from collections import Counter
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    C = Counter(A)
    ans = 0
    for i in C:
        ans += C[i] * (C[i] - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()