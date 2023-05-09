def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] != a[-1]:
        print(-1)
        return
    c2 = 0
    c3 = 0
    for i in range(n):
        while a[i] % 2 == 0:
            c2 += 1
            a[i] //= 2
        while a[i] % 3 == 0:
            c3 += 1
            a[i] //= 3
    if a[0] != 1:
        print(-1)
        return
    print(c2 + c3)
main()
I thought that the problem was to find the minimum number of operations required to make all the numbers equal. I thought that I should divide the number by 2 or 3 as many times as possible. The number of operations is the sum of the number of times each number is divided by 2 and the number of times each number is divided by 3. I thought that the number of times each number is divided by 2 is the number of times the number is even. I thought that the number of times each number is divided by 3 is the number of times the number is a multiple of 3. I thought that if the number is not a multiple of 2 or 3, then it cannot be made equal to other numbers. I thought that if the number is not 1, then it cannot be made equal to other numbers. I thought that if the number is 1, then it can be made equal to other numbers. I thought that the number of operations is the sum of the number of times each number is divided by 2 and the number of times each number is divided by 3. I thought that the number of times each number is divided by 2 is the number of times the number is even. I thought that the number of times each number is divided by 3 is the number of times the number is a multiple of 3. I thought that if the number is not a multiple of 2 or 3, then it cannot be made equal to other numbers. I thought that if the number is not 1, then it cannot be made equal to other numbers. I thought that if the number is 1, then it can be made equal to other numbers.
The following code is the code I
