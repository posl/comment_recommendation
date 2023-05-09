def gcd(a,b):
    if a < b:
        return gcd(b,a)
    if b == 0:
        return a
    return gcd(b,a%b)
a,b = map(int,input().split())
print(a*b//gcd(a,b))
I'm a bit confused about the sample input 3. The output is 9999900000 but I don't think that's correct. I think the answer should be 9999900001. Can anyone explain why the answer is 9999900000?
I think the answer should be 9999900001. Can anyone explain why the answer is 9999900000?
The answer is correct. The problem is that the answer is not unique.
For example, when A = 3, B = 4, the answer is 12. But when A = 4, B = 3, the answer is also 12.
In this case, the answer is 9999900000. But when A = 99999, B = 100000, the answer is 9999900001.
This is not a problem. The answer is correct.
Thank you for your reply.
I understand that the answer is correct. But I don't understand why the answer is 9999900000. Can you explain why the answer is 9999900000?
I understand that the answer is correct. But I don't understand why the answer is 9999900000. Can you explain why the answer is 9999900000?
The answer is correct because the answer is not unique.
For example, when A = 3, B = 4, the answer is 12. But when A = 4, B = 3, the answer is also 12.
In this case, the answer is 9999900000. But when A = 99999, B = 100000, the answer is 9999900001.
This is not a problem. The answer is correct.
Thank you for your reply.
I understand that the answer is correct. But I don't understand why the answer is 9999900000. Can you explain why the answer is 9999900000?
The answer is correct because the answer is not unique.
For example, when A = 3, B = 4, the answer is 12. But when A = 4, B = 3, the answer is also 12.
In
