Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = input()
    ans = 0
    for i in range(len(N)):
        for j in range(len(N)):
            if i == j:
                continue
            x = int(N[:i+1])
            y = int(N[i+1:j+1])
            if x == 0 or y == 0:
                continue
            ans = max(ans, x*y)
    print(ans)

=======
Suggestion 2

def main():
    n = input()
    ans = 0
    for i in range(1, len(n)):
        a = int(n[0:i])
        b = int(n[i:len(n)])
        if ans < a * b:
            ans = a * b
    print(ans)

=======
Suggestion 3

def main():
    N = input()
    N_len = len(N)
    N_int = int(N)
    N_list = [int(i) for i in N]
    if N_len == 2:
        print(N_list[0] * N_list[1])
        return
    if N_len == 3:
        print(N_list[0] * N_list[1] * N_list[2])
        return
    if N_len == 4:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3])
        return
    if N_len == 5:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4])
        return
    if N_len == 6:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5])
        return
    if N_len == 7:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6])
        return
    if N_len == 8:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7])
        return
    if N_len == 9:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7] * N_list[8])
        return
    if N_len == 10:
        print(N_list[0] * N_list[1] * N_list[2] * N_list[3] * N_list[4] * N_list[5] * N_list[6] * N_list[7] * N_list[8] * N_list[9])
        return

=======
Suggestion 4

def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = int("".join(N))
    print(N)
    return

=======
Suggestion 5

def split(a):
    s=str(a)
    res=[]
    for i in range(len(s)-1):
        res.append((int(s[:i+1]),int(s[i+1:])))
    return res

n=int(input())
res=0
for i,j in split(n):
    res=max(res,i*j)
print(res)

=======
Suggestion 6

def solve():
    n = input()
    ans = 0
    for i in range(1,len(n)):
        a = int(n[:i])
        b = int(n[i:])
        ans = max(ans, a*b)
    print(ans)

=======
Suggestion 7

def main():
    N = input()
    max = 0
    for i in range(1,len(N)):
        a = int(N[0:i])
        b = int(N[i:len(N)])
        if max < a*b:
            max = a*b
    print(max)

=======
Suggestion 8

def main():
    N = int(input())
    N_str = str(N)
    N_len = len(N_str)
    N_list = list(N_str)
    N_list.sort(reverse=True)
    N_list_1 = N_list[0:N_len//2]
    N_list_2 = N_list[N_len//2:N_len]
    N_1 = int("".join(N_list_1))
    N_2 = int("".join(N_list_2))
    print(N_1*N_2)

=======
Suggestion 9

def solve():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        A = int(N[:i])
        B = int(N[i:])
        ans = max(ans, A * B)
    print(ans)

=======
Suggestion 10

def main():
    N = input()
    ans = 0
    for i in range(1, len(N)):
        ans = max(ans, (int(N[:i]) * int(N[i:])))
    print(ans)
