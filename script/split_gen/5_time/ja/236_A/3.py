def main():
    s = input()
    a, b = map(int, input().split())
    print(s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:])
