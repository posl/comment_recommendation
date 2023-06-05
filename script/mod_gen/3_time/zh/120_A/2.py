def main():
    #input
    a, b, c = map(int, input().split())
    #calculate
    if a * c <= b:
        ans = c
    else:
        ans = b // a
    #output
    print(ans)

if __name__ == '__main__':
    main()