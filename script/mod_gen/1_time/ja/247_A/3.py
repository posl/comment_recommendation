def main():
    S = input()
    S = S.replace("1","2")
    S = S.replace("0","1")
    S = S.replace("2","0")
    print(S)

if __name__ == '__main__':
    main()