def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N - 1):
        if S[i] == S[i + 1]:
            happy += 1
    print(min(happy + 2 * K, N - 1))
