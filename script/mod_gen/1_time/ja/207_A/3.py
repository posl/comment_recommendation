def main():
    abc = list(map(int, input().split()))
    abc.sort()
    print(abc[1] + abc[2])

if __name__ == '__main__':
    main()