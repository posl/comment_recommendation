def main():
    x = float(input())
    if x < 0:
        print(int(x-0.5))
    else:
        print(int(x+0.5))

if __name__ == '__main__':
    main()