def main():
    S = input()
    ans = 10**9
    for i in range(len(S)-2):
        ans = min(ans,abs(753-int(S[i:i+3])))
    print(ans)
