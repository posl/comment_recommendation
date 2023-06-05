def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = str(i+1)
    print(" ".join(b))

if __name__ == '__main__':
    main()