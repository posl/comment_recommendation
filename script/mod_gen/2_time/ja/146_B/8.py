def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    for i in S:
        #print(i)
        if ord(i)+N > 90:
            print(chr(ord(i)+N-26),end="")
        else:
            print(chr(ord(i)+N),end="")

if __name__ == '__main__':
    main()