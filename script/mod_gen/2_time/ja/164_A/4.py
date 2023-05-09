def main():
    #input
    S, W = map(int, input().split())
    
    #output
    if W >= S:
        print("unsafe")
    else:
        print("safe")

if __name__ == '__main__':
    main()