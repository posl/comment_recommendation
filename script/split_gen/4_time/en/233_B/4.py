def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = reversed(s[l-1:r])
    print(''.join(s))
