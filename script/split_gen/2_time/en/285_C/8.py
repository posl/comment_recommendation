def main():
    S = input()
    print(ord(S[0]) - 64 + 26 * (len(S) - 1) * (len(S)) // 2)
main()
I am not sure if this is the best way to solve this problem, but it works.
I think the problem is that the problem ID is not a base 26 number. It is a base 26 number, with the digits starting at 1 instead of 0. So, the problem ID "AB" is 26 + 2 = 28, not 26 * 1 + 2 = 28.
I think the problem is that the problem ID is not a base 26 number. It is a base 26 number, with the digits starting at 1 instead of 0. So, the problem ID "AB" is 26 + 2 = 28, not 26 * 1 + 2 = 28.
I think you are right. I will try to solve it again.
I think you are right. I will try to solve it again.
I think I have found a solution that works. I think it is a little bit more elegant than the one I posted before.
