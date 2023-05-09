def main():
    S = input()
    print(max(len(x) for x in S.split('S')))

if __name__ == '__main__':
    main()