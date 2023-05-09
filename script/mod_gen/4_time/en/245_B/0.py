def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = set(a)
    for i in range(2001):
        if i not in s:
            print(i)
            break

if __name__ == '__main__':
    main()