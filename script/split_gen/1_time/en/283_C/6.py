def main():
    S = input()
    if S == '0':
        print(1)
        return
    ans = 0
    for i, s in enumerate(S):
        if s == '0':
            continue
        ans += 1
        if i == len(S) - 1:
            continue
        ans += (len(S) - i - 1) // 2
    print(ans)
