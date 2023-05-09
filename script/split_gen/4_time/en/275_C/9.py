def main():
    import sys
    from collections import Counter
    input = sys.stdin.readline
    S = [input().rstrip() for _ in range(9)]
    S = [Counter(s) for s in S]
    cnt = 0
    for i in range(9):
        cnt += S[i]["#"]
    print(cnt)
