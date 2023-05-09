def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * 200001
    for a in A:
        B[a] += 1
    ans = 0
    for i in range(200001):
        if B[i] >= 2:
            ans += B[i] * (B[i] - 1) // 2
    for a in A:
        print(ans - (B[a] - 1))
main()
I s

if __name__ == '__main__':
    main()