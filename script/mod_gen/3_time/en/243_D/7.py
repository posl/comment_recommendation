def sol():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'U':
            x = (x+1)//2
        elif s[i] == 'L':
            x = 2*x-1
        else:
            x = 2*x
    print(x)

if __name__ == '__main__':
    sol()