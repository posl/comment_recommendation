def main():
    l, r = map(int, input().split())
    s = list(input())
    s[l-1:r] = s[l-1:r][::-1]
    print("".join(s))
