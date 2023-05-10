def main():
    w = int(input())
    if w <= 2:
        print("NO")
    elif w % 2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()