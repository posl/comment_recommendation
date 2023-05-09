def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    b = []
    for i in range(n):
        b.append(a[:i] + a[i+1:])
    for i in range(n):
        print(max(b[i]))

if __name__ == '__main__':
    main()