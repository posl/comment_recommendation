def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(1, n+1):
        if a[i-1] != i:
            print('No')
            return
    print('Yes')
