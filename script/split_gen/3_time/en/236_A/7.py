def swap(S,a,b):
    S=list(S)
    S[a],S[b]=S[b],S[a]
    return ''.join(S)
S=input()
a,b=map(int,input().split())
print(swap(S,a-1,b-1))
The first line of input is the string S.
The second line of input is the two integers a and b.
After swapping the a-th and b-th characters from the beginning of S and print the resulting string.
The first line of output is the string after swapping the a-th and b-th characters from the beginning of S.
Sample Input 1
chokudai
3 5
Sample Output 1
chukodai
Sample Input 2
aa
1 2
Sample Output 2
aa
Sample Input 3
aaaabbbb
1 8
Sample Output 3
baaabbba
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int, input().split())
S = list(S)
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
S = input()
a, b = map(int,
