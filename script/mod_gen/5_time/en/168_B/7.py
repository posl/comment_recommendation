def main():
    k = int(input())
    s = input()
    if len(s) > k:
        s = s[:k] + "..."
    print(s)

if __name__ == '__main__':
    main()