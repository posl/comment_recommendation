def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = [A[i] + B[i] for i in range(N)]
    AB_sorted = sorted(AB, reverse=True)
    A_sorted = sorted(A, reverse=True)
    B_sorted = sorted(B, reverse=True)
    AB_rank = [0] * N
    A_rank = [0] * N
    B_rank = [0] * N
    for i in range(N):
        AB_rank[i] = AB_sorted.index(AB[i]) + 1
        A_rank[i] = A_sorted.index(A[i]) + 1
        B_rank[i] = B_sorted.index(B[i]) + 1
    AB_rank_sorted = sorted(AB_rank)
    A_rank_sorted = sorted(A_rank)
    B_rank_sorted = sorted(B_rank)
    AB_rank_sorted = AB_rank_sorted[:X+Y+Z]
    A_rank_sorted = A_rank_sorted[:X]
    B_rank_sorted = B_rank_sorted[:Y]
    AB_rank_sorted.sort()
    A_rank_sorted.sort()
    B_rank_sorted.sort()
    AB_rank_sorted = [i-1 for i in AB_rank_sorted]
    A_rank_sorted = [i-1 for i in A_rank_sorted]
    B_rank_sorted = [i-1 for i in B_rank_sorted]
    AB_rank_sorted = set(AB_rank_sorted)
    A_rank_sorted = set(A_rank_sorted)
    B_rank_sorted = set(B_rank_sorted)
    AB_rank_sorted = list(AB_rank_sorted)
    A_rank_sorted = list(A_rank_sorted)
    B_rank_sorted = list(B_rank_sorted)
    AB_rank_sorted.sort()
    A_rank_sorted.sort()
    B_rank_sorted.sort()
    AB_rank_sorted = [i+1 for i in AB_rank_sorted]
    A_rank_sorted = [i+1 for i in A_rank_sorted]
    B_rank_sorted = [i+1 for i in B_rank_sorted]
    AB_rank_sorted = set(AB_rank_sorted)
    A_rank_sorted = set(A_rank_sorted)
    B_rank_sorted = set(B_rank_sorted)
    AB_rank_sorted = list(AB_rank_sorted)
    A_rank_sorted = list(A_rank_sorted)
    B_rank_sorted = list(B_rank_sorted)
    AB_rank_sorted.sort
