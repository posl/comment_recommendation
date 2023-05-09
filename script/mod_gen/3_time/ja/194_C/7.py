def main():
    N = int(input())
    A = list(map(int,input().split()))
    A2 = [a**2 for a in A]
    A3 = [a**3 for a in A]
    A4 = [a**4 for a in A]
    A2_sum = sum(A2)
    A3_sum = sum(A3)
    A4_sum = sum(A4)
    ans = 0
    for i in range(N):
        ans += (i*A2[i] - A3_sum)
        ans += (A2_sum - (N-i-1)*A2[i])
        A2_sum -= A2[i]
        A3_sum -= A3[i]
    print(ans)

if __name__ == '__main__':
    main()