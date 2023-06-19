def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for _ in range(Q):
        x, k = map(int, input().split())
        print(find_kth(A, x, k))
