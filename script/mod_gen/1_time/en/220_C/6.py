def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    
    sum_a = sum(a)
    sum_a100 = sum_a * 100
    
    if sum_a100 < x:
        print(-1)
        return
    
    k = 0
    s = 0
    for i in range(100):
        for j in range(n):
            s += a[j]
            k += 1
            if s > x:
                print(k)
                return

if __name__ == '__main__':
    main()