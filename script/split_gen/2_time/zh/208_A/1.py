def main():
    n = int(input())
    S = []
    T = []
    for i in range(n):
        a,b = map(int,input().split())
        S.append([a,b])
    for i in range(n):
        a,b = map(int,input().split())
        T.append([a,b])
    if S == T:
        print('Yes')
    else:
        print('No')
