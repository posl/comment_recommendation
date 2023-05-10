def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(S.rfind('a')+1)

if __name__ == '__main__':
    main()