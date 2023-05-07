def main():
    s = input()
    if len(s) != 9:
        print("Input length is not 9")
        return
    for i in range(10):
        if str(i) not in s:
            print(i)
            return

if __name__ == '__main__':
    main()