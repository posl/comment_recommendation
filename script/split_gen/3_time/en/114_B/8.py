def main():
    S = input()
    S = S + '0'
    L = len(S)
    ans = 1000
    for i in range(L-2):
        x = int(S[i:i+3])
        ans = min(ans, abs(753 - x))
    print(ans)
