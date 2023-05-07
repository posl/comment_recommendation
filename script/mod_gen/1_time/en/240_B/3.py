def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    a = set(a)
    print(len(a))

if __name__ == '__main__':
    main()