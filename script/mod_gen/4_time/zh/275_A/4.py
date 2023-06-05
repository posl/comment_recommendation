def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    print(h.index(max(h))+1)

if __name__ == '__main__':
    main()