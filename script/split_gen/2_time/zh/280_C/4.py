def main():
    n = input()
    s = raw_input().split()
    s = [int(x) for x in s]
    a = [0 for i in range(n)]
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - a[i-1]
    print ' '.join(map(str, a))
