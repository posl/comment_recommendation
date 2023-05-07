def main():
    s = input()
    print(max(s.count('0'), s.count('1')) * 2)

if __name__ == '__main__':
    main()