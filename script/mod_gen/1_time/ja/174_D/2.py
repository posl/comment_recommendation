def main():
    N = int(input())
    S = input()
    S = S.replace("R","0").replace("W","1")
    S = S.replace("0","2").replace("1","0").replace("2","1")
    print(min(S.count("01"),S.count("10")))

if __name__ == '__main__':
    main()