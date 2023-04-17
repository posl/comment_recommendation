Synthesizing 10/10 solutions

=======

def main():
    N = int(input())
    if N == 1 or N == 2 or N == 3 or N == 5 or N == 6:
        print("No")
    else:
        print("Yes")

=======

def main():
    n = int(input())
    for i in range(0, n // 4 + 1):
        for j in range(0, n // 7 + 1):
            if 4 * i + 7 * j == n:
                print("Yes")
                return
    print("No")

=======

def main():
    n = int(input())
    for i in range(n//4+1):
        for j in range(n//7+1):
            if 4*i + 7*j == n:
                print("Yes")
                return
    print("No")

main()

import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0;i<=n/4;i++){
            for(int j=0;j<=n/7;j++){
                if(4*i + 7*j == n){
                    System.out.println("Yes");
                    return;
                }
            }
        }
        System.out.println("No");
    }
}

=======

def main():
    N = int(input())
    for i in range(N+1):
        for j in range(N+1):
            if 4*i + 7*j == N:
                print('Yes')
                return
    print('No')

=======

def main():
    N = int(input())
    for i in range(0, N//4+1):
        for j in range(0, N//7+1):
            if 4*i+7*j == N:
                print("Yes")
                return
    print("No")

main()

I am trying to write a function that will take a string and return a dictionary of the number of times each letter appears in the string. The function should ignore case, and it should ignore any characters that are not a letter. For example, given the string "Hello, World!" the function should return the dictionary {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.

I am having trouble with the part where I need to ignore the characters that are not letters. I am trying to use ord() to get the ASCII value of each character and then check if it is between 65 and 90 or 97 and 122. But I am not sure how to use ord() in the for loop. I have tried several different ways, but I keep getting errors. Please help! Thank you!

=======

def main():
    n = int(input())
    for i in range(0, n+1, 4):
        if (n - i) % 7 == 0:
            print("Yes")
            return
    print("No")

=======

def main():
    N = int(input())
    print("Yes" if N % 4 == 0 or N % 7 == 0 or N % 4 == 2 and N % 7 == 2 else "No")

=======

def main():
    N = int(input())
    if N < 4:
        print('No')
    elif N % 2 == 0:
        print('Yes')
    elif N % 4 == 1:
        print('No')
    elif N % 4 == 3:
        print('Yes')

=======

def findSolution(N):
    for i in range(0, N//4+1):
        for j in range(0, N//7+1):
            if 4*i + 7*j == N:
                return "Yes"
    return "No"

=======

def main():
    N = int(input())
    # Write your code here
    for i in range(0,N+1):
        for j in range(0,N+1):
            if (i*4 + j*7) == N:
                print('Yes')
                return
    print('No')
    return
