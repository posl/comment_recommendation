def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if s[0] == t[0] and s[n-1] == t[m-1]:
        print('Yes')
    else:
        print('No')
