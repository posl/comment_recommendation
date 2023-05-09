def main():
    N = int(input())
    for i in range(N//4+1):
        if (N - 4*i) % 7 == 0:
            print("Yes")
            return
    print("No")
main()
I'm not sure if this is the right place to ask this, but I'm not sure where else to go. I'm trying to learn Python, and I'm stuck on a problem that I can't seem to figure out. I'm using Python 3.6.1. I'm trying to make a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)
When I run it, it prints 0. I'm not sure what I'm doing wrong. I've tried using +=, but that doesn't work either. I've also tried using a while loop, but that doesn't work either. Any help would be appreciated.
I'm trying to write a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(sum)
When I run it, it prints 0. I'm not sure what I'm doing wrong. I've tried using +=, but that doesn't work either. I've also tried using a while loop, but that doesn't work either. Any help would be appreciated.
I am having a hard time understanding how to write a program that will take a number and print the sum of all the numbers from 1 to that number. For example, if I input 5, it would print 15, because 1+2+3+4+5 = 15. Here is my code:
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num

if __name__ == '__main__':
    main()