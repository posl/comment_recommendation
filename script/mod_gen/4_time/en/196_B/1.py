def main():
    x = input()
    if "." in x:
        print(int(x.split(".")[0]))
    else:
        print(x)

if __name__ == '__main__':
    main()