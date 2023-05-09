def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 1:
        print(0)
        return
    A.sort()
    A = A[::-1]
    B = [A[0]]
    for i in range(1, N):
        if A[i] < B[-1]:
            B.append(A[i])
        else:
            B.append(B[-1])
    print(sum(A) - sum(B))
    return

if __name__ == '__main__':
    main()