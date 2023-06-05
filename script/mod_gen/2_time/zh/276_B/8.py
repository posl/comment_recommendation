def main():
    s = input()
    a = s.rfind('a')
    print(a+1 if a != -1 else -1)

if __name__ == '__main__':
    main()