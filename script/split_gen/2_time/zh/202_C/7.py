def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    cnt = 0
    for i in range(n):
        cnt += b.count(c[a[i]-1])
    print(cnt)
main()
