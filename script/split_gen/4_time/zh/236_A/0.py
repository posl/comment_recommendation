def main():
    s = raw_input()
    a,b = map(int,raw_input().split())
    print s[:a-1]+s[b-1]+s[a:b-1]+s[a-1]+s[b:]
