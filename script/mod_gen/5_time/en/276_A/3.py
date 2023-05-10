def main():
    s = input()
    if s.find('a') >= 0:
        print(s.rfind('a')+1)
    else:
        print(-1)

if __name__ == '__main__':
    main()