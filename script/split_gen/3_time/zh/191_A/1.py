def main():
    v,t,s,d = map(int, input().split())
    if d/(v*t) >= 1 and d/(v*s) <= 1:
        print('No')
    else:
        print('Yes')
