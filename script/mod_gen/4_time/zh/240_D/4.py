def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A = [3, 2, 3, 2, 2]
    # A = [2, 3, 2, 3, 3, 3, 2, 3, 3, 2]
    B = [0] * 200001
    for a in A:
        B[a] += 1
    # print(B)
    ans = 0
    for i in range(200001):
        if B[i] > 0:
            ans += 1
            B[i] -= 1
        if B[i] > 0:
            B[i + 1] += B[i]
    print(ans)

if __name__ == '__main__':
    main()