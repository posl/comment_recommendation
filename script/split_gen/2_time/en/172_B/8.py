def main():
    import sys
    from collections import defaultdict
    def input(): return sys.stdin.readline().rstrip()
    S = input()
    T = input()
    cnt = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            cnt += 1
    print(cnt)
