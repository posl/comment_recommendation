def main():
    N,M = map(int,input().split())
    balls = [0]*(2*N)
    for i in range(M):
        k = int(input())
        a = list(map(int,input().split()))
        for j in range(k):
            balls[2*i+j] = a[j]
    for i in range(N):
        if balls.count(i+1) != 2:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()