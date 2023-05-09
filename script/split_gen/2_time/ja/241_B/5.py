def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    
    for i in range(m):
        if b[i] > a[i]:
            print('No')
            return
    print('Yes')
