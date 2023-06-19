def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [a % 200 for a in A]
    C = [0] * 200
    for b in B:
        C[b] += 1
    ans = 0
    for c in C:
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()