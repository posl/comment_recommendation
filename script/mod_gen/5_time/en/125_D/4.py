def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [abs(x) for x in a]
    if sum([1 for x in a if x < 0]) % 2 == 0:
        print(sum(b))
    else:
        print(sum(b) - 2 * min(b))

if __name__ == '__main__':
    main()