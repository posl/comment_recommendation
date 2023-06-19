Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    A = [0]
    for i in range(N):
        if S[i] == 'L':
            A.insert(i, i+1)
        else:
            A.insert(i+1, i+1)
    print(' '.join(map(str, A)))

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(' '.join(map(str, a)))

=======
Suggestion 3

def main():
    N = int(input())
    S = input()

    A = [0]
    for i in range(N):
        if S[i] == "L":
            A.insert(0, i+1)
        else:
            A.append(i+1)

    print(" ".join(map(str, A)))

=======
Suggestion 4

def main():
    n = int(input())
    s = input()

    # 0のリストを作成
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i + 1)
        else:
            a.append(i + 1)

    # 結果を出力
    print(*a)

=======
Suggestion 5

def problems237_d():
    pass

=======
Suggestion 6

def solve():
    N=int(input())
    S=input()
    ans=[]
    left=0
    right=0
    for i in range(N):
        if S[i]=='L':
            ans.insert(left+1,i+1)
            left+=1
        else:
            ans.append(i+1)
            right+=1
    for i in ans:
        print(i,end=' ')

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    ans = [0]
    for i in range(1,N):
        if S[i-1] == 'L':
            ans.insert(0,i)
        else:
            ans.append(i)
    print(*ans)
