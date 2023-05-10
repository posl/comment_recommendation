def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    S = input().rstrip()
    n = len(S)
    ans = 0
    for i in range(n):
        ans += (ord(S[i])-64) * 26 ** (n-i-1)
    print(ans)
