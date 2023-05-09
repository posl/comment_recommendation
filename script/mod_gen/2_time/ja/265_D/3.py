def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "No"
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if P * A[i] + Q * A[j] + R * A[k] == P * A[i] + Q * A[j] + R * A[k]:
                    ans = "Yes"
    print(ans)

if __name__ == '__main__':
    main()