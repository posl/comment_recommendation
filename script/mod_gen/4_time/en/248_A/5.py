def main():
    s = input()
    a = set(s)
    for i in range(10):
        if str(i) not in a:
            print(i)
            break

if __name__ == '__main__':
    main()