def main():
    N = int(input())
    S = list(map(int,input().split()))
    A = [S[0]]
    for i in range(1,N):
        A.append(S[i]-A[i-1])
    print(*A)

if __name__ == '__main__':
    main()