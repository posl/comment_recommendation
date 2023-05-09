def ABC(S):
    ABC = 0
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            for k in range(j+1,len(S)):
                if S[i] == 'A' and S[j] == 'B' and S[k] == 'C':
                    ABC += 1
    return ABC
S = input()
S = S.replace('?', 'A')
ABC1 = ABC(S)
S = S.replace('A', 'B')
ABC2 = ABC(S)
S = S.replace('B', 'C')
ABC3 = ABC(S)
print((ABC1 + ABC2 + ABC3) % 1000000007)
I got 50/100 points for this code. I am getting the correct answer for the first 2 test cases but not for the 3rd one. Can someone please help me with this?
I am new to the forums and I am not sure if this is the right place to post this question. I would be grateful if someone could help me with this.
Thanks in advance.
Your code is so slow, that it's not even worth optimizing. You're getting 50/100 because your code times out on the last test case. You should try to optimize your code, or use a different approach.

if __name__ == '__main__':
    ABC()