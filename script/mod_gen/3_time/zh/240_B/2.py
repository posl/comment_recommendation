def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(len(set(a)))

if __name__ == '__main__':
    main()