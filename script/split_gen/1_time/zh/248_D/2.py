def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        count = 0
        for i in range(L-1, R):
            if A[i] == X:
                count += 1
        print(count)
