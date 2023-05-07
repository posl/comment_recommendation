def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    print((N // (A + B)) * A + min(N % (A + B), A))
