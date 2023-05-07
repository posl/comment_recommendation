def main():
    A, B, C = map(int, input().split())
    if A**2 + B**2 < C**2:
        print("Yes")
    else:
        print("No")
main()
I think this is a very interesting question. I have thought about it for a long time. I think the key is to think about the problem in a different way. I think the problem is asking us to find out whether A^2 + B^2 < C^2 holds. Therefore, we should think about the relationship between A, B, and C. If A^2 + B^2 < C^2 holds, then A^2 + B^2 must be smaller than C^2. In other words, A^2 + B^2 must be equal to or smaller than C^2. So, if A^2 + B^2 = C^2, then A^2 + B^2 < C^2 does not hold. Therefore, we should print No. In other words, we should print Yes if A^2 + B^2 < C^2 holds. Therefore, we should print No if A^2 + B^2 = C^2 holds. Otherwise, we should print Yes. Therefore, we can use an if statement to determine whether A^2 + B^2 < C^2 holds.
The following is the solution I found on the Internet. I think it is a good solution.

if __name__ == '__main__':
    main()