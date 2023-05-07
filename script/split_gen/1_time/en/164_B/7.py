def main():
    A,B,C,D = map(int,input().split())
    takahashi = (C-1)//B
    aoki = (A-1)//D
    if takahashi <= aoki:
        print('Yes')
    else:
        print('No')
