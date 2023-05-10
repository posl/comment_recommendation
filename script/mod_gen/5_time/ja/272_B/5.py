def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(M)]
    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if i+1 not in A[k] or j+1 not in A[k]:
                    break
            else:
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()