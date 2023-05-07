def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(4 * N - 1):
        B[A[i]] += 1
    for i in range(1, N + 1):
        if B[i] % 2 == 1:
            print(i)
            return
main()
I got the following error message:
Traceback (most recent call last):
  File "main.py", line 26, in <module>
    main()
  File "main.py", line 24, in main
    print(i)
  File "main.py", line 24, in main
    print(i)
  File "main.py", line 24, in main
    print(i)
  [Previous line repeated 981 more times]
  File "main.py", line 22, in main
    if B[i] % 2 == 1:
RecursionError: maximum recursion depth exceeded in comparison
I am not sure why I am getting this error. I am not sure if it is because I am using recursion.
Can someone please help me understand what is wrong with my code and how I can fix it?
Thanks in advance.
I want to know how to use recursion in this problem.
I have a string of length n. I want to find the number of distinct substrings of that string. The substrings can be overlapping.
I am trying to solve this problem using recursion. I have divided the problem into two parts.
1. If the first character of the string is not equal to the last character, then the number of distinct substrings will be the number of distinct substrings of the string without the first character plus the number of distinct substrings of the string without the last character.
2. If the first character of the string is equal to the last character, then the number of distinct substrings will be the number of distinct substrings of the string without the first character plus the number of distinct substrings of the string without the last character plus 1.
I am not sure if this is the correct approach to solve this problem. Please help me understand the problem and how to solve it.
Thanks in advance.
I am trying to solve this problem using recursion. I am not sure if this is the correct approach to solve this problem. Please help me understand the problem and how to solve

if __name__ == '__main__':
    main()