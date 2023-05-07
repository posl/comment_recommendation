def main():
    n = input()
    if n[0] == n[1] and n[1] == n[2]:
        print(n)
    else:
        print(str(int(n[0])+1)*3)

if __name__ == '__main__':
    main()