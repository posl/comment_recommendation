def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        if i == 0:
            P = 0
        else:
            P = P + A[i-1]
    print(P)
main()
My code is giving me a runtime error. Can anyone help me with this?
I am not sure why you are using an if statement to check if i is 0. If i is 0, then the second line of code in the for loop will not run. So, the first time the loop runs, P will be equal to 0. I think you should remove the if statement and just set P to 0 before the for loop. Also, you are adding A[i-1] to P each time you run the for loop. I think you should add A[i] to P each time you run the for loop. I think this will fix your problem.
I am not sure why you are using an if statement to check if i is 0. If i is 0, then the second line of code in the for loop will not run. So, the first time the loop runs, P will be equal to 0. I think you should remove the if statement and just set P to 0 before the for loop. Also, you are adding A[i-1] to P each time you run the for loop. I think you should add A[i] to P each time you run the for loop. I think this will fix your problem.
Thanks for the advice. I tried it and it worked. I got the correct answer and it was accepted.

if __name__ == '__main__':
    main()