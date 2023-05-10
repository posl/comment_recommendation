def main():
    n,m,x,t,d = map(int, input().split())
    h = x * d + t
    for i in range(x+1, n):
        h += d
    for i in range(x-1, m):
        h -= d
    print(h)

if __name__ == '__main__':
    main()