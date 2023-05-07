def main():
    n = int(input())
    a = list(map(int, input().split()))
    if len(a) != n:
        print('No')
        exit()
    a.sort()
    for i in range(n):
        if a[i] != i + 1:
            print('No')
            exit()
    print('Yes')
    exit()
