def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    print(h.index(max(h))+1)

if __name__ == '__main__':
    main()