def main():
    S = input()
    K = int(input())
    #print(S, K)
    for i in range(0, K):
        if S[i] == '1':
            continue
        else:
            print(S[i])
            break
    else:
        print(S[K-1])
main()
I think the problem is that it is not printing the first character in the string, but I am not sure how to fix it.
I am trying to make a program that will take a number and print it in a column. For example, if the number is 123456789, it will print it like this:
1
2
3
4
5
6
7
8
9
I am having trouble with the numbers that are more than one digit. I can get it to print the first digit of the number, but then it will print the second digit on the same line as the first. I have tried using if statements to see if the number is more than one digit, but it didn't work. I am not sure how to fix this problem.
Here is my code:

if __name__ == '__main__':
    main()