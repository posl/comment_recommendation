def main():
    a, b, c, d = map(int, input().split())
    print((a + b) * (c - d))
    print("Takahashi")
main()
This is the code I have written. I am getting the correct output for the first two test cases, but for the third test case, I am getting the wrong answer. I am getting the output as 4000 instead of 40000. Can anyone help me to figure out what I am doing wrong?
Thank you in advance.
Your name to display (optional):
Your name to display (optional):
The problem is with the last line of your code. You have written print("Takahashi") . But the question asks you to print Takahashi (without any quotes). So, you can simply remove the quotes.
Your name to display (optional):
You have to write the code such that ...READ MORE
You can use t

if __name__ == '__main__':
    main()