def main():
    s = input()
    print(min(abs(int(s[i:i+3])-753) for i in range(len(s)-2)))

if __name__ == '__main__':
    main()