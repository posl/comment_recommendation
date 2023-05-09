def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    
    print(sum % 998244353)

if __name__ == '__main__':
    main()