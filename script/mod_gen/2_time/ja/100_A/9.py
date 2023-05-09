def main():
    a,b = map(int, input().split())
    if (a+b) > 16:
        print(":( ")
    else:
        print("Yay!")

if __name__ == '__main__':
    main()