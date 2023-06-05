def main():
    N, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(0)
    A.append(0)
    for i in range(N):
        for j in range(i+1, N+1):
            if A[i] == A[j]:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()