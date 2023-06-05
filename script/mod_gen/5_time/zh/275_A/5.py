def main():
    n = int(input())
    h = input().split()
    h = [int(i) for i in h]
    print(h.index(max(h))+1)

if __name__ == '__main__':
    main()