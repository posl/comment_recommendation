def main():
    #input
    S,W = map(int,input().split())
    #output
    if S <= W:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()