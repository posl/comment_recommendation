def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_max = max(a)
    a_max_index = a.index(a_max)
    for i in range(n):
        if i == a_max_index:
            print(sorted(a[:a_max_index]+a[a_max_index+1:])[-1])
        else:
            print(a_max)

if __name__ == '__main__':
    main()