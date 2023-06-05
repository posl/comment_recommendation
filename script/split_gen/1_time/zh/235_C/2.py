def main():
    N, Q = map(int, input().split())
    A = [int(_) for _ in input().split()]
    for _ in range(Q):
        x, k = map(int, input().split())
        count = 0
        for i in range(N):
            if A[i] == x:
                count += 1
                if count == k:
                    print(i+1)
                    break
        else:
            print(-1)
