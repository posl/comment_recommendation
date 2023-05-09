def main():
    s = input()
    s = set(s)
    for i in range(10):
        if not str(i) in s:
            print(i)
            break

if __name__ == '__main__':
    main()