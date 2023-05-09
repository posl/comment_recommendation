def main():
    N = int(input())
    if N == 0:
        print(0)
        return
    S = []
    while N != 0:
        if N % 2 == 0:
            S.append(0)
            N = N // -2
        else:
            S.append(1)
            N = (N - 1) // -2
    for i in range(len(S)-1, -1, -1):
        print(S[i], end="")
    print()
