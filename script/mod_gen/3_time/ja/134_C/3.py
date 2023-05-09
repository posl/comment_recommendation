def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        max_a = max(a)
        if a[i] == max_a:
            a[i] = max(a[0:i] + a[i+1:n])
        print(a[i])

if __name__ == '__main__':
    main()