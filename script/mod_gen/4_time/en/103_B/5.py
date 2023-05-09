def main():
    s = input()
    t = input()
    if s == t:
        print('Yes')
    else:
        for i in range(len(s) - 1):
            s = s[-1] + s[:-1]
            if s == t:
                print('Yes')
                break
        else:
            print('No')
main()
This is my code. I have tried 2 test cases and it worked. But when I tried to submit, it shows WA. Can anyone help me out?
I think you should use the else clause of your for loop to print No, rather than using a for-else construct. The for-else construct will only run if the for loop is not broken out of, but you break out of the loop if you find a match. So, the else clause will never run.
Thanks for the reply. I tried that but it still shows WA. I am not sure what is wrong with my code. Can you please check my code and tell me if there is any error?
I think I see the problem. You are checking if s == t, but you need to check if s == t after each rotation. Try this:

if __name__ == '__main__':
    main()