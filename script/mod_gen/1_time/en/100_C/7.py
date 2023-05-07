def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while all(ai % 2 == 0 for ai in a):
        a = [ai // 2 for ai in a]
        count += 1
    print(count)

if __name__ == '__main__':
    main()