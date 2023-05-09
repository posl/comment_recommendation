def main():
    H, W, N = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    
    a = list(set(a))
    b = list(set(b))
    a.sort()
    b.sort()
    for i in range(N):
        print(a.index(a[i])+1, b.index(b[i])+1)
main()
I am a newbie in Python. I am trying to solve the above problem. I am stuck at the last test case. It is not giving me the correct output. Can you please help me to find the error in my code?
I am using Python 3.6.5
I am not sure why you are sorting a and b . You only need to sort them if you want to find the minimum number of operations required to get the output. In this problem, you just need to find the final position of the cards.
You can use a dictionary to store the position of the cards.
a = {1: 3, 2: 2}
b = {1: 2, 2: 5}
for i in range(N):
    print(a[i+1], b[i+1])
Thanks for your reply. I have tried your code. But it is not giving me the correct output. I am still getting the same error.
I have solved the problem. I have used a dictionary to store the position of the cards. Thanks for your help.
I am glad you found the solution. Please consider marking the answer as accepted. That way, it will be easier for other people to find the solution.
I am trying to solve the above problem. I am stuck at the last test case. It is not giving me the correct output. Can you please help me to find the error in my code?
I am not sure what you mean by “last test case”. The sample input and output you provided are not the same.
I am trying to solve the above problem. I am stuck at the last test case. It is not giving me the correct output. Can you please help me to find the error in my code?
I am not sure what you mean by “last test case”. The sample input and output you provided are not the same.
I have updated the sample input and output. Please check it.
I have solved the problem

if __name__ == '__main__':
    main()