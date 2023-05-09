def main():
    n = int(input())
    L = list(map(int, input().split()))
    L.sort()
    if L[n-1] < sum(L[:n-1]):
        print('Yes')
    else:
        print('No')
