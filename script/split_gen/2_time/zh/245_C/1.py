def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    for i in range(n):
        if abs(a[i] - b[i]) > k:
            print('No')
            exit()
    print('Yes')
