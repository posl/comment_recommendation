def main():
    x = float(input())
    if x - int(x) >= 0.0 and x - int(x) <= 0.2:
        print(int(x) - 1)
    elif x - int(x) >= 0.3 and x - int(x) <= 0.6:
        print(int(x))
    elif x - int(x) >= 0.7 and x - int(x) <= 0.9:
        print(int(x) + 1)

if __name__ == '__main__':
    main()