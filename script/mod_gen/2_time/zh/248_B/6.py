def main():
    s = input()
    s = list(s)
    s.sort()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

if __name__ == '__main__':
    main()