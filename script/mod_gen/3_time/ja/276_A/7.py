def main():
    s = input()
    print(len(s) - s[::-1].index('a') - 1 if 'a' in s else -1)

if __name__ == '__main__':
    main()