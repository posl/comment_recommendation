def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(abs(get_index(p, n) - get_index(q, n)))

if __name__ == '__main__':
    main()