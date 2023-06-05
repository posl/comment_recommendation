def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans += (ord(S[i])-ord('A')+1)*(26**(len(S)-i-1))
    print(ans)
