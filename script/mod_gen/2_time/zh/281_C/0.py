def main():
    n,t = map(int, input().split())
    a = list(map(int, input().split()))
    
    t = t % sum(a)
    
    for i in range(n):
        if t < a[i]:
            break
        t -= a[i]
    print(i+1,t)

if __name__ == '__main__':
    main()