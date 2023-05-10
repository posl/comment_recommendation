def main():
    p = list(map(int, input().split()))
    ans = [None] * 26
    for i in range(26):
        ans[p[i] - 1] = chr(ord('a') + i)
    print(''.join(ans))
