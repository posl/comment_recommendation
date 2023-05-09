def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    max_a = max(a)
    max_a_index = a.index(max_a)
    for i in range(n):
        if i == max_a_index:
            print(max(a[:i]+a[i+1:]))
        else:
            print(max_a)

if __name__ == '__main__':
    main()