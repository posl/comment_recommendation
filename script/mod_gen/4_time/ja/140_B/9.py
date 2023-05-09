def main():
    # coding: utf-8
    # Your code here!
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    total = 0
    for i in range(n):
        total += b[a[i]-1]
        if i > 0 and a[i]-1 == a[i-1]:
            total += c[a[i-1]-1]
    
    print(total)

if __name__ == '__main__':
    main()