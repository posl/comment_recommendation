def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    print(a.index(a_sorted[1])+1)

if __name__ == '__main__':
    main()