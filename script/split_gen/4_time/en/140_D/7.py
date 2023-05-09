def main():
    N, K = map(int, input().split())
    S = input()
    S = S + "R"
    count = 0
    for i in range(N):
        if S[i] == S[i+1]:
            count += 1
    print(min(N-1, count+2*K))
