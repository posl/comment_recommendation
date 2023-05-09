def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in a:
        c[i-1] += 1
    s = sum(c)
    for i in a:
        print((s-c[i-1])*(c[i-1]-1)//2)

if __name__ == '__main__':
    main()