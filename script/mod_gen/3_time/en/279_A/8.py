def main():
    #get input
    s = input()
    #count number of bottoms
    count = 0
    for i in range(len(s)-1):
        if s[i] == "v" and s[i+1] == "v":
            count += 1
    #print result
    print(count)
main()

if __name__ == '__main__':
    main()