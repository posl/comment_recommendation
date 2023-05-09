def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    r = S.count("R")
    w = N-r
    if r == 0 or w == 0:
        print(0)
    else:
        print(min(r,w))

if __name__ == '__main__':
    main()