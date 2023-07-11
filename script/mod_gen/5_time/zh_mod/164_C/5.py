def main():
    n = int(input())
    item = set()
    for i in range(n):
        item.add(input())
    print(len(item))

if __name__ == '__main__':
    main()