def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    for i in range(n):
        if a[i] == a_max:
            a[i] = -1
    a_max = max(a)
    for i in range(n):
        if a[i] == -1:
            print(a_max)
        else:
            print(a_max)

if __name__ == '__main__':
    main()