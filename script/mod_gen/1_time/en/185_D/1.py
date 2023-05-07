def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(0)
    A.append(N+1)
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    B = []
    for i in range(M+1):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    if len(B) == 0:
        print(0)
        return
    k = min(B)
    for i in range(len(B)):
        B[i] = B[i]//k
        if B[i] == 0:
            B[i] = 1
    print(sum(B))
main()
I got 100 points. The code is pretty straightforward. The idea is to first find the gaps between the blue squares. Then, choose the minimum gap as k. Then, we can use the stamp k times to cover all the gaps.

if __name__ == '__main__':
    main()