def main():
    n = input()
    nlist = n.split()
    nset = set(nlist)
    if len(nset) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()