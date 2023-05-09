def main():
    S = input()
    print(S.rfind('a')+1 if 'a' in S else -1)

if __name__ == '__main__':
    main()