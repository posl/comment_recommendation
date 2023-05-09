def main():
    N = int(input())
    H = list(map(int, input().split()))
    max_h = 0
    count = 0
    for h in H:
        if h >= max_h:
            max_h = h
            count += 1
    print(count)
main()

if __name__ == '__main__':
    main()