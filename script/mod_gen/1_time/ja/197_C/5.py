def main():
    N = int(input())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N):
        ans = ans | A[i]
    print(ans^A[0])
main()

if __name__ == '__main__':
    main()