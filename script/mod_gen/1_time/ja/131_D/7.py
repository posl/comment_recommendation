def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = list(reversed(A))
    B = list(reversed(B))
    t = 0
    for i in range(N):
        if t <= B[i]:
            t = B[i]
        else:
            t -= t % A[i]
        if t > B[i]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()