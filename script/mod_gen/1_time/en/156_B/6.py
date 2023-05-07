def main():
    n, k = map(int, input().split())
    print(len(str(n).replace("0", "")) + 1)

if __name__ == '__main__':
    main()