def main():
    n = int(input())
    names = []
    for i in range(n):
        name = input().split()
        if name not in names:
            names.append(name)
        else:
            print("Yes")
            exit()
    print("No")

if __name__ == '__main__':
    main()