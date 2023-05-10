def main():
    s = input()
    s = sorted(s)
    for i in range(0,10):
        if str(i) not in s:
            print(i)
            return

if __name__ == '__main__':
    main()