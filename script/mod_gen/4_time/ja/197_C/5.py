def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        or_temp = 0
        for j in range(i, N):
            or_temp = or_temp | A[j]
            xor_temp = ans ^ or_temp
            if xor_temp < ans:
                break
            else:
                ans = xor_temp
    print(ans)

if __name__ == '__main__':
    main()