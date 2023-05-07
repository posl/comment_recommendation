def main():
    S = input()
    T = input()
    #S = "cupofcoffee"
    #T = "cupofhottea"
    #S = "abcde"
    #T = "bcdea"
    #S = "apple"
    #T = "apple"
    count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()