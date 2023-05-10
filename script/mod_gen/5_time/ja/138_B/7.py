def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_inv = [1 / x for x in a]
    print(1 / sum(a_inv))

if __name__ == '__main__':
    main()