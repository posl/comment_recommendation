def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort()
    b.sort()
    b.reverse()
    
    if a[0] > b[0]:
        print("No")
        return
    
    for i in range(n):
        if a[i] + b[i] > k:
            print("No")
            return
    
    print("Yes")
    return

if __name__ == '__main__':
    main()