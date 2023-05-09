def main():
    n = int(input())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == 0:
        print(-1)
    else:
        print(odd)

if __name__ == '__main__':
    main()