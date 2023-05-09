def main():
    N = int(input())
    S = input()
    ans = ""
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',' and count % 2 == 0:
            ans += '.'
        else:
            ans += S[i]
    print(ans)
