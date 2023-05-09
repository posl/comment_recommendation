def main():
    N = int(input())
    ans = -1
    for i in range(N):
        A, P, X = map(int, input().split())
        if X > A:
            if ans == -1:
                ans = P
            else:
                ans = min(ans, P)
    print(ans)
main()
I've been trying to solve this problem for a while now, and I'm not sure what I'm doing wrong. I've tried using the following code:

if __name__ == '__main__':
    main()