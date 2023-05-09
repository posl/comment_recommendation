def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            count += 1
    if count > K:
        print(N - 1 - (count - K))
    else:
        print(N - 1)
