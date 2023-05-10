def main():
    x = input().rstrip()
    if "." in x:
        x = x.split(".")[0]
    print(x)

if __name__ == '__main__':
    main()