def main():
    x = input()
    if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
        print("Weak")
    elif int(x[0]) == (int(x[1]) + 1) % 10 and int(x[1]) == (int(x[2]) + 1) % 10 and int(x[2]) == (int(x[3]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()