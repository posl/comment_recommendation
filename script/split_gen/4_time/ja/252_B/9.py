def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if A[-1] > B[-1]:
        print('Yes')
    else:
        print('No')
