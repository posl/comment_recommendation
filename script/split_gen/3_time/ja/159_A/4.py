def main():
    N, M = map(int, input().split())
    if N == 0 or M == 0:
        print(0)
        return
    if N == 1 and M == 1:
        print(0)
        return
    if N == 1:
        print(M - 1)
        return
    if M == 1:
        print(N - 1)
        return
    print(N * M - N - M)
