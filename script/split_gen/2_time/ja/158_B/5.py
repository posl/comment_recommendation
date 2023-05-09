def main():
    N, A, B = map(int, input().split())
    q, r = divmod(N, A+B)
    print(A*q + min(A, r))
