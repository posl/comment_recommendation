def main():
    N = input()
    keta = len(N)
    #print(keta)
    N = int(N)
    if N%3 == 0:
        print(0)
        return
    elif keta == 1:
        print(-1)
        return
    elif keta == 2:
        if N%10 == 0 or N%10 == 5:
            print(1)
            return
        else:
            print(-1)
            return
    else:
        #print(N%3)
        #print(N%10)
        #print(N%10)
        #print(N%100)
        #print(N%1000)
        #print(N%10000)
        #print(N%100000)
        #print(N%1000000)
        #print(N%10000000)
        #print(N%100000000)
        #print(N%1000000000)
        #print(N%10000000000)
        #print(N%100000000000)
        #print(N%1000000000000)
        #print(N%10000000000000)
        #print(N%100000000000000)
        #print(N%1000000000000000)
        #print(N%10000000000000000)
        #print(N%100000000000000000)
        #print(N%1000000000000000000)
        if N%3 == 1:
            if N%10 == 1 or N%100 == 1 or N%1000 == 1 or N%10000 == 1 or N%100000 == 1 or N%1000000 == 1 or N%10000000 == 1 or N%100000000 == 1 or N%1000000000 == 1 or N%10000000000 == 1 or N%100000000000 == 1 or N%1000000000000 == 1 or N%10000000000000 == 1 or N%100000000000000 == 1 or N%1000000000000000 == 1 or N%10000000000000000 == 1 or N%100000000000000000 == 1 or N%1000000000000000000 == 1:
                print(1)
                return
            else:
                if keta ==

if __name__ == '__main__':
    main()