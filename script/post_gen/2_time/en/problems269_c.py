Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    N_bin = bin(N)
    N_bin = N_bin[2:]
    N_bin = N_bin[::-1]
    for i in range(2**len(N_bin)):
        i_bin = bin(i)
        i_bin = i_bin[2:]
        i_bin = i_bin[::-1]
        flag = True
        for j in range(len(i_bin)):
            if i_bin[j] == '1':
                if j >= len(N_bin):
                    flag = False
                    break
                if N_bin[j] == '0':
                    flag = False
                    break
        if flag:
            print(i)

=======
Suggestion 2

def main():
    N = int(input())
    b = bin(N)[2:]
    b = b[::-1]
    for i in range(2**len(b)):
        c = bin(i)[2:]
        c = c[::-1]
        if len(c) < len(b):
            c += "0" * (len(b) - len(c))
        ans = 0
        for j in range(len(c)):
            if c[j] == "1" and b[j] == "1":
                ans += 2**j
        print(ans)

=======
Suggestion 3

def solve(n):
    if n == 0:
        print(0)
        return
    ans = []
    for i in range(60):
        if n >> i & 1:
            ans.append(i)
    for i in range(2**len(ans)):
        tmp = 0
        for j in range(len(ans)):
            if i >> j & 1:
                tmp += 1 << ans[j]
        print(tmp)

=======
Suggestion 4

def main():
    N = int(input())
    for i in range(2**15):
        if N & i == i:
            print(i)

=======
Suggestion 5

def main():
    N = int(input())
    for i in range(1 << 60):
        if i & N == i:
            print(i)

=======
Suggestion 6

def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    bit = bin(N)[2:]
    bit = bit[::-1]
    print(0)
    for i in range(len(bit)):
        if bit[i] == "1":
            print(1 << i)
    return

=======
Suggestion 7

def main():
    N = int(input())
    N_bin = bin(N)[2:]
    N_bin = N_bin[::-1]
    N_bin = N_bin + "0"*(60-len(N_bin))
    N_bin = N_bin[::-1]
    N_bin = N_bin[2:]
    N_bin = N_bin[::-1]
    #print(N_bin)
    for i in range(2**60):
        i_bin = bin(i)[2:]
        i_bin = i_bin[::-1]
        i_bin = i_bin + "0"*(60-len(i_bin))
        i_bin = i_bin[::-1]
        i_bin = i_bin[2:]
        i_bin = i_bin[::-1]
        #print(i_bin)
        if len(i_bin) <= len(N_bin):
            if N_bin[:len(i_bin)] == i_bin:
                print(i)
        else:
            if i_bin == N_bin[:len(i_bin)]:
                print(i)

=======
Suggestion 8

def main():
    n = int(input())
    b = bin(n)[2:]
    b = '0'*(60-len(b)) + b
    b = b[::-1]
    pos = []
    for i in range(len(b)):
        if b[i] == '1':
            pos.append(i)
    for i in range(2**len(pos)):
        ans = 0
        for j in range(len(pos)):
            if (i >> j) & 1:
                ans += 2**pos[j]
        print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    B = bin(N)[2:]
    B = B[::-1]
    B = B + "0" * (60 - len(B))
    B = B[::-1]
    for i in range(2 ** 15):
        S = bin(i)[2:]
        S = S[::-1]
        S = S + "0" * (15 - len(S))
        S = S[::-1]
        ans = 0
        for j in range(60):
            if S[j] == '1' and B[j] == '0':
                break
            if S[j] == '1':
                ans += 2 ** j
        else:
            print(ans)

=======
Suggestion 10

def f(s, n):
    if len(s) == 0:
        print(n)
        return
    for i in range(len(s)):
        f(s[:i]+s[i+1:], n+s[i])

s = bin(int(input()))[2:]
f(s, 0)
