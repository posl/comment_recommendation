def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    ans = [i for i in range(N+1)]
    for i in range(Q-1, -1, -1):
        ans[x[i]], ans[x[i]+1] = ans[x[i]+1], ans[x[i]]
    for i in range(1, N+1):
        print(ans[i], end=' ')
main()
The code above is a solution for the above problem. The following is the explanation of the code.

if __name__ == '__main__':
    main()