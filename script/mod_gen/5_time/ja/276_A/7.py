def main():
    S = input()
    if S.find('a') != -1:
        print(S.rfind('a')+1)
    else:
        print(-1)

if __name__ == '__main__':
    main()