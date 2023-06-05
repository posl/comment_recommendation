def main():
    N,K = map(int,input().split())
    AB = [map(int,input().split()) for _ in range(N)]
    A,B = [list(i) for i in zip(*AB)]
    A.append(10**100)
    B.append(0)
    from bisect import bisect_left
    index = bisect_left(A,K)
    print(B[index-1])
