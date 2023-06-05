def main():
    n,m = map(int,input().split())
    S = input().split()
    T = input().split()
    for i in range(n):
        if S[i] in T:
            print('Yes')
        else:
            print('No')
