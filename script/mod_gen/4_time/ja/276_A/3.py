def main():
    s = input()
    if "a" not in s:
        print(-1)
    else:
        print(s.rfind("a")+1)

if __name__ == '__main__':
    main()