def main():
    n = int(input())
    s, t = input().split()
    print("".join(s[i] + t[i] for i in range(n)))
main()

if __name__ == '__main__':
    main()