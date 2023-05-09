def main():
    T = int(input())
    for _ in range(T):
        a,s = map(int,input().split())
        if a > s:
            print('No')
        elif a == s:
            print('Yes')
        elif a*2 > s:
            print('Yes')
        else:
            print('No')
