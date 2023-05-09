def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(1, N):
        if A[i-1] == A[i]:
            print("NO")
            return
    print("YES")
main()

if __name__ == '__main__':
    main()