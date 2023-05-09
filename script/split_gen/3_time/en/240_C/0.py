def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print('Yes' if any(X % a == 0 and X // a <= N or X % b == 0 and X // b <= N or X % a == 0 and X % b == 0 and X // a + X // b <= N for a, b in zip(A, B)) else 'No')
