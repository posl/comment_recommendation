def main():
    S = input()
    N = len(S)
    #print(S)
    #print(N)
    red = 0
    blue = 0
    for i in range(N):
        if S[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue)*2)

if __name__ == '__main__':
    main()