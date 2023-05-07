def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range(1,m+1):
    flag=0
    for j in range(n):
        if gcd(i,a[j])==1:
            flag+=1
    if flag==n:
        ans.append(i)
print(len(ans))
for i in ans:
    print(i)
I am not able to solve the problem. Please help me out.
I have a doubt regarding the last line of the code. Why are we printing the length of the list ans ?
Because the first line of the output is the number of integers satisfying the requirement. You can see the sample input and output in the question.
Hey, I am new to competitive programming. I am trying to solve this problem. I have written the code but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to solve the problem but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to solve the problem but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to solve the problem but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to solve the problem but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to solve the problem but I am getting wrong answer. Can you please check my code and help me out. Here is the link to my code. https://ideone.com/2Z1u3x
I have the same doubt. I am trying to
