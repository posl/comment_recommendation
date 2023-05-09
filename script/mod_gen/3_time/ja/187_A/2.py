def main():
    A, B = map(int, input().split())
    a = [int(i) for i in str(A)]
    b = [int(i) for i in str(B)]
    print(max(sum(a), sum(b)))

if __name__ == '__main__':
    main()