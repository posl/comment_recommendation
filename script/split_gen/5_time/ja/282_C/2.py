def main():
    N = int(input())
    S = input()
    cnt = 0
    ans = ""
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif cnt%2 == 1 and S[i] == ',':
            ans += '.'
        else:
            ans += S[i]
    print(ans)
