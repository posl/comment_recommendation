def main():
    N = int(input())
    T = list(map(int, input().split()))
    T.sort()
    T.reverse()
    A = 0
    B = 0
    for i in range(N):
        if A > B:
            B += T[i]
        else:
            A += T[i]
    print(max(A, B))
