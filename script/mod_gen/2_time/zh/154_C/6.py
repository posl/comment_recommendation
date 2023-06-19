def main():
    N = int(input())
    A = input().split()
    if len(A) != N:
        return
    A = list(map(int, A))
    A.sort()
    for i in range(N-1):
        if A[i] == A[i+1]:
            print("NO")
            return
    print("YES")

if __name__ == '__main__':
    main()