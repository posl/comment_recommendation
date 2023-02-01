#Problem Statement
#Takahashi is a cashier.
#There is a cash register with 11 keys: 00, 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. The cash register initially displays 0. 
#Whenever he types the key 00, the displayed number is multiplied by 100; whenever he types one of the others, the displayed number is multiplied by 10, and then added by the number written on the key.
#Takahashi wants the cash register to display an integer S. At least how many keystrokes are required to make it display S?
#
#Constraints
#1≤S≤10^100000
#S is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#S
#
#Output
#Print the answer in a line.
#
#Sample Input 1
#40004
#
#Sample Output 1
#4
#
#Sample Input 2
#1355506027
#
#Sample Output 2
#10
#
#Sample Input 3
#10888869450418352160768000001
#
#Sample Output 3
#27

def main():
    S = input()
    if len(S) == 1:
        print(1)
    else:
        print(len(S))

if __name__ == '__main__':
    main()