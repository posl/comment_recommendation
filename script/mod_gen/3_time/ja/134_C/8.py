def main():
    n = int(input())
    a = [int(input()) for i in range(n)]
    max_a = max(a)
    max_a2 = max(a)
    for i in a:
        if i == max_a:
            max_a2 = max(a)
            print(max_a2)
        else:
            print(max_a)

if __name__ == '__main__':
    main()