def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        print(n - binary_search(a, x))

if __name__ == '__main__':
    main()