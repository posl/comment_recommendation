def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    while all(num % 2 == 0 for num in a):
        a = [num / 2 for num in a]
        count += 1
    print(count)

if __name__ == '__main__':
    main()