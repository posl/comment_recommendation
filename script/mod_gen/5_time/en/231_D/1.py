def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] < B[0] and A[-1] < B[0]:
        print("Yes")
    elif A[-1] < B[-1] and A[0] < B[-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()