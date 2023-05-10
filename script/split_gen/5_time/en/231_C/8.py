def main():
    N, Q = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    for i in range(Q):
        x = int(input())
        idx = bisect.bisect_left(H, x)
        print(N - idx)
