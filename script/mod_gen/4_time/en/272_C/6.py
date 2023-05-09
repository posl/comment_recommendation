def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    s = set()
    for i in range(N):
        for j in range(i+1, N):
            if (A[i]+A[j])%2==0:
                s.add(A[i]+A[j])
                break
    if len(s)==0:
        print(-1)
    else:
        print(max(s))

if __name__ == '__main__':
    main()