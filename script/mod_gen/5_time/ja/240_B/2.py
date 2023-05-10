def main():
    n = int(input())
    a = list(map(int, input().split()))
    set_a = set(a)
    print(len(set_a))

if __name__ == '__main__':
    main()