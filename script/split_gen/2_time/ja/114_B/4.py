def main():
    S = input()
    N = len(S)
    ans = 1000
    for i in range(N-2):
        ans = min(ans, abs(int(S[i:i+3]) - 753))
    print(ans)
