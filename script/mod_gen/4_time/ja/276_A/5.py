def main():
    s = input()
    try:
        print(s.rindex('a') + 1)
    except ValueError:
        print(-1)

if __name__ == '__main__':
    main()