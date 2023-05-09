def main():
    W = int(input())
    if W == 2 or W == 3:
        print("NO")
    elif W % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()