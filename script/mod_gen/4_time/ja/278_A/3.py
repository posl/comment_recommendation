def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a.pop(0)
        a.append(0)
    for i in a:
        print(i, end=' ')
    print()

if __name__ == '__main__':
    main()