def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A)]
    A.sort(reverse=True)
    B = A[:2**N]
    B.sort(key=lambda x: x[1])
    print(B[1][1]+1)
