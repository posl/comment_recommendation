def main():
    N = int(input())
    print(str(N)[-2:])
main()
I want to get the last two digits of a number.
I tried the following code. It works. But I am not sure if this is the best solution.
N = input()
print(N[-2:])
I think it is the best solution. You can also use %100
N = input()
print(N%100)
The first solution is better in my opinion. If I have a number with 10 digits I will have to do N%10000000000 and then N%1000000000 to get the last two digits. It is better to just use N[-2:] .
I think it is better to use %100 because it is more general. You can use it for any number of digits.
I think it is better to use %100 because it is more general. You can use it for any number of digits.
I agree, but I think the question is about last two digits.
The question is about the last two digits. But the answer is not.
N = input()
print(N%100)
The answer is not. The answer is 01 . The last two digits of 101 are 01, which should be printed.
N = input()
print(N%100)
The answer is not. The answer is  01 . The last two digits of  101  are  01, which should be printed.
I think you are right. I did not read the question carefully.
I think you are right. I did not read the question carefully.
I think it is the best solution. You can also use %100
N = input()
print(N%100)
I think it is the best solution. You

if __name__ == '__main__':
    main()