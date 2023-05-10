def main():
    S = input()
    S = list(map(int, S))
    ans = 1000
    for i in range(len(S)-2):
        tmp = S[i]*100 + S[i+1]*10 + S[i+2]
        ans = min(ans, abs(753-tmp))
    print(ans)
