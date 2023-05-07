def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    ans = [0] * (N+1)
    for i in range(N):
        ans[0] += 1
        ans[0] -= 1
        ans[B[i]] += 1
    for i in range(N):
        ans[i+1] += ans[i]
    for i in range(N):
        print(ans[i],end=" ")
    print()

if __name__ == '__main__':
    main()