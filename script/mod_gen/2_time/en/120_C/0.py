def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)
main()

if __name__ == '__main__':
    main()