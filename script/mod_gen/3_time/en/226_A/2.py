def main():
    x = float(input())
    if x - int(x) < 0.5:
        print(int(x))
    else:
        print(int(x)+1)

if __name__ == '__main__':
    main()