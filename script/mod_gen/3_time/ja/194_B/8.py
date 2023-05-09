def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    min_time = 10**6
    for i in range(N):
        for j in range(N):
            if i == j:
                time = A[i]+B[j]
            else:
                time = max(A[i],B[j])
            if min_time > time:
                min_time = time
    print(min_time)

if __name__ == '__main__':
    main()