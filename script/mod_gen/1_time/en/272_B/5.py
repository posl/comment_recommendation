def main():
    n, m = map(int, input().split())
    a = [set(map(int, input().split()[1:])) for _ in range(m)]
    print('YNeos'[any(a[i] & a[j] == set() for i in range(m) for j in range(i+1, m))::2])

if __name__ == '__main__':
    main()