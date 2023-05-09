def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] != i+1:
            print('No')
            return
    print('Yes')
    return
