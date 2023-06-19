def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == len(a):
        a.sort()
        for i in range(n):
            if a[i] != i+1:
                print('No')
                exit()
        print('Yes')
    else:
        print('No')
