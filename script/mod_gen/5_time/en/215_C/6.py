def main():
    s, k = input().split()
    k = int(k)
    s = sorted(s)
    print(s[k-1])

if __name__ == '__main__':
    main()