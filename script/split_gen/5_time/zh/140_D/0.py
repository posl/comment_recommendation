def main():
    N, K = map(int, input().split())
    S = input()
    S = list(S)
    S.append("E")
    count = 0
    for i in range(0, N):
        if S[i] == S[i+1]:
            count += 1
    count = min(count + 2 * K, N - 1)
    print(count)
