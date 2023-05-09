def main():
    N = input()
    if len(set(N)) == 1:
        print(N)
    else:
        print(str(int(N[0])+1)*3)

if __name__ == '__main__':
    main()