def main():
    S = input().split()
    T = input().split()
    S.sort()
    T.sort()
    if S == T:
        print('Yes')
    else:
        print('No')
