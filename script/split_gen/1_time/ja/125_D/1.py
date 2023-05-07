def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N):
        if i % 2 == 0:
            B.append(A[i])
        else:
            B.append(A[i] * -1)
    print(sum(B))
main()
