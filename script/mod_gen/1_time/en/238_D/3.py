def main():
    T = int(input())
    for i in range(T):
        a,s = map(int,input().split())
        if a > s:
            print("No")
        elif (s-a)%2 == 0:
            print("Yes")
        else:
            print("No")
main()
The code above is a solution to the problem above. I have tried to explain the code as much as possible. If you have any questions, do not hesitate to ask. I hope this helps.
Thank you for reading.

if __name__ == '__main__':
    main()