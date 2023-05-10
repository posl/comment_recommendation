def main():
    N, K = map(int, input().split())
    S = input()
    happy = 0
    for i in range(N-1):
        if S[i] == S[i+1]:
            happy += 1
    print(min(N-1, happy + K*2))
