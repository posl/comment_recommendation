def main():
    #input
    N = int(input())
    #compute
    if N % 10 == 3:
        ans = "bon"
    elif N % 10 in [0,1,6,8]:
        ans = "pon"
    else:
        ans = "hon"
    #output
    print(ans)

if __name__ == '__main__':
    main()