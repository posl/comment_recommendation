def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[A[i]-1] = i+1
    for i in range(N):
        print(ans[i],end=' ')

if __name__ == '__main__':
    main()