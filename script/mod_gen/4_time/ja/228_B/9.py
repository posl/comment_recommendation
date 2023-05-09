def main():
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N,X,A)
    ans = 0
    for i in range(N):
        if X == A[i]:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()