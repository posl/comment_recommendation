def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    print(int("".join(N[0:2])) * int("".join(N[2:4])))

if __name__ == '__main__':
    main()