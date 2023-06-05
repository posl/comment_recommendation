def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    print('Yes')
    for i in range(1,n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')
    print('Yes')
