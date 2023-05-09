def main():
    S = input()
    x = len(set(S))
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        print(6)

if __name__ == '__main__':
    main()