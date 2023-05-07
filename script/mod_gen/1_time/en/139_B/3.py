def main():
    #input
    A, B = map(int, input().split())
    #compute
    if B % A == 0:
        ans = B // A
    else:
        ans = B // A + 1
    #output
    print(ans)

if __name__ == '__main__':
    main()