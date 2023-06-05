def main():
    s = input()
    print(len(s) * (len(s) - 1) * (len(s) - 2) // 6)

if __name__ == '__main__':
    main()