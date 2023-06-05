def main():
    n = input()
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        print(int(n[0])*111)

if __name__ == '__main__':
    main()