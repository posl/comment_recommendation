def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        l = 0
        for j in range(1, N - i + 1):
            if S[j - 1] != S[j - 1 + i]:
                l = j
        print(l)
