def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if A + B > N:
        print(N // (A + B) * A + min(N % (A + B), A))
    else:
        print(N // (A + B) * A + min(N % (A + B), A))
