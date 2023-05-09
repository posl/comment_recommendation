def is_palindrome(s):
    return s == s[::-1]
S = input()
for i in range(len(S)):
    if is_palindrome(S[i:]):
        print('Yes')
        exit()
print('No')
I used this code to solve this problem. However, the time limit is exceeded. Can anyone help me?
The time complexity of your code is O(N^2) . This is because you are checking whether a string is a palindrome or not, which has a time complexity of O(N) , and you are doing this for N times.
You can use KMP algorithm to solve this problem. The time complexity of KMP algorithm is O(N) , so it can pass the time limit.
Here is a reference to the KMP algorithm.
KMP algorithm
@kotetsu_kun Thank you for your advice. I will try it.
@kotetsu_kun I have tried to solve this problem using KMP algorithm. However, I don't know how to solve it. Can you help me?
I am not good at KMP algorithm. I don't know how to solve it. Can you help me?
I think you can use the KMP algorithm to solve this problem. Here is a reference to the KMP algorithm.
