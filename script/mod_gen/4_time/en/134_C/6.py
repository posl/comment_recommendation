def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_value = max(a)
    for i in range(n):
        if a[i] == max_value:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_value)

if __name__ == '__main__':
    main()