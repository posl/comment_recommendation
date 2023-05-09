def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == '1':
            ans += 1
        else:
            break
    if ans == len(S):
        print(ans)
    else:
        print(ans+1)
