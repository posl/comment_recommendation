def main():
    s = input()
    for i in range(1, 10):
        if str(i) not in s:
            print(i)
            exit()

if __name__ == '__main__':
    main()