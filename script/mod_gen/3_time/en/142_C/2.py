def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = [0]*N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(" ".join(map(str,ans)))

if __name__ == '__main__':
    main()