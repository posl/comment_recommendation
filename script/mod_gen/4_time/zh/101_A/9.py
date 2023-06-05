def main():
    #input
    s = input()
    #init
    res = 0
    #process
    for i in s:
        if i == "+":
            res += 1
        elif i == "-":
            res -= 1
        else:
            print("input error")
            return
    #output
    print(res)
    return

if __name__ == '__main__':
    main()