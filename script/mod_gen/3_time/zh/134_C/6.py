def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    for i in range(n):
        if a[i] == max_a:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_a)

if __name__ == '__main__':
    main()