def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        B[i] = A[i]%200
    C = [0]*200
    for i in range(N):
        C[B[i]] += 1
    ans = 0
    for i in range(200):
        ans += C[i]*(C[i]-1)//2
    print(ans)
main()
I don't know why I got this error. I tried to submit this code to AtCoder, but I got this error.
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from problems200_c import main
  File "/home/runner/work/AtCoder/AtCoder/AtCoder Beginner Contest 200/problems200_c.py", line 1
    # Path: problems200_c.py
    ^
SyntaxError: invalid syntax
If you want to use Python 3.8, you need to set the language version to Python 3.8.
If you want to use Python 3.8, you need to set the language version to Python 3.8.
Thank you for your reply.
I tried to set the language version to Python 3.8, but I got this error.
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from problems200_c import main
  File "/home/runner/work/AtCoder/AtCoder/AtCoder Beginner Contest 200/problems200_c.py", line 1
    # Path: problems200_c.py
    ^
SyntaxError: invalid syntax
I used Python 3.8.2 on my PC, and I didn't get any error. I also used Python 3.8.2 on the AtCoder, but I got this error.
I don't know why I got this error.
I think that the error is caused by the fact that I used the comment at the beginning of the code.
I removed the comment and I got this error.
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    from problems200_c import main
  File "/home/runner/work/AtCoder/AtCoder/AtCoder Beginner Contest 200/problems200_c.py", line 1
    # Path

if __name__ == '__main__':
    main()