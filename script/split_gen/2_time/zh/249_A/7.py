def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for i in range(Q):
        L, R, X = map(int, input().split())
        count = 0
        for j in range(L-1, R):
            if A[j] == X:
                count += 1
        print(count)
