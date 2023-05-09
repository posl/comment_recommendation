def main():
    N = int(input())
    L = list(map(int,input().split()))
    maxL = max(L)
    sumL = sum(L)-maxL
    if maxL < sumL:
        print('Yes')
    else:
        print('No')
