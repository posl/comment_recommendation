def main():
    #input
    N = int(input())
    #compute
    if N==1:
        ans = 0
    elif N==2:
        ans = 1
    else:
        ans = 0
        for i in range(2,N+1):
            ans += (i-1)*(N//i)
            ans += max(0,(N%i)-(i//2))
    #output
    print(ans)
main()
I got a WA for this code. I don't understand why. Can someone help me with this?
I have the following code:

if __name__ == '__main__':
    main()