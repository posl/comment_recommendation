def main():
    N = int(input())
    #print(N)
    if N%4==0 or N%7==0:
        print("Yes")
    else:
        for i in range(1,15):
            if N-4*i>0 and (N-4*i)%7==0:
                print("Yes")
                return
            elif N-7*i>0 and (N-7*i)%4==0:
                print("Yes")
                return
        print("No")

if __name__ == '__main__':
    main()