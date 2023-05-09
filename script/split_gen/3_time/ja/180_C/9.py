def main():
    import sys
    input = sys.stdin.readline
    n = int(input())
    i = 1
    ans = []
    while i * i <= n:
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)
        i += 1
    ans = sorted(list(set(ans)))
    print(*ans, sep='\n')
