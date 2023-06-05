def main():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[:k] + "...")
    else:
        print(s)

if __name__ == '__main__':
    main()