def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n):
        b.insert(a[i]-1, i+1)
    print(" ".join(map(str, b)))

if __name__ == '__main__':
    main()