def main():
    line = input()
    if line[0] == line[1] == line[2] == line[3]:
        print("Weak")
    elif int(line[1]) == (int(line[0]) + 1) % 10 and int(line[2]) == (int(line[1]) + 1) % 10 and int(line[3]) == (int(line[2]) + 1) % 10:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()