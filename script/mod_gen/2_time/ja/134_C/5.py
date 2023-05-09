def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max_idx = A.index(A_max)
    A2 = A.copy()
    A2.pop(A_max_idx)
    A2_max = max(A2)
    for i in range(N):
        if i == A_max_idx:
            print(A2_max)
        else:
            print(A_max)

if __name__ == '__main__':
    main()