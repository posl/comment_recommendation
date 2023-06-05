def main():
    x = input()
    if '.' in x:
        print(int(float(x)+0.5))
    else:
        print(x)

if __name__ == '__main__':
    main()