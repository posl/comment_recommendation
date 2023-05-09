def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a')+1)
    else:
        print(-1)

if __name__ == '__main__':
    main()