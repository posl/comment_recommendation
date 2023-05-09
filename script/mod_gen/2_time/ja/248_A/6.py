def main():
    s = input()
    s = list(s)
    s.sort()
    for i in range(9):
        if s[i] == str(i):
            continue
        else:
            print(i)
            break

if __name__ == '__main__':
    main()