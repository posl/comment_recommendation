def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a - i - 1 for i, a in enumerate(A)]
    A.sort()
    b = A[N // 2]
    print(sum([abs(a - b) for a in A]))
