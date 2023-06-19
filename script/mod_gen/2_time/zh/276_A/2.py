def main():
    s = input()
    if s.rfind('a') != -1:
        print(s.rfind('a') + 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()