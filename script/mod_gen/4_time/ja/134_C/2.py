def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(max(a[:i] + a[i+1:]))
        else:
            print(a_max)

if __name__ == '__main__':
    main()