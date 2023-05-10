def main():
    H, W, N = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(list(set(A)))
    B = sorted(list(set(B)))
    A_dict = {}
    B_dict = {}
    for i in range(len(A)):
        A_dict[A[i]] = i+1
    for i in range(len(B)):
        B_dict[B[i]] = i+1
    for i in range(N):
        print(A_dict[A[i]], B_dict[B[i]])

if __name__ == '__main__':
    main()