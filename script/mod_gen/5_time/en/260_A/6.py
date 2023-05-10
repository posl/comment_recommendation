def main():
    S = input()
    for i in S:
        if S.count(i) == 1:
            print(i)
            break
    else:
        print(-1)

if __name__ == '__main__':
    main()