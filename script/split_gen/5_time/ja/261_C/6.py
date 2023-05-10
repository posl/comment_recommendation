def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    n = int(readline())
    d = {}
    for _ in range(n):
        s = readline().rstrip().decode('utf-8')
        if s not in d:
            d[s] = 0
        d[s] += 1
        print(s if d[s] == 1 else s+'('+str(d[s]-1)+')')
