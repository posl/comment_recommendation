def main():
    s = input()
    s = list(s)
    s = [int(i) for i in s]
    for i in range(1,10):
        if i not in s:
            print(i)
            return

if __name__ == '__main__':
    main()