def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0,0)
    A.insert(0,0)
    A.insert(N+3,0)
    A.insert(N+3,0)
    cnt = 0
    for i in range(2,N+2):
        if A[i-1] == i-1 and A[i+1] == i+1:
            cnt += 1
    for i in range(2,N+2):
        if A[i-1] == i+1 and A[i+1] == i-1:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()