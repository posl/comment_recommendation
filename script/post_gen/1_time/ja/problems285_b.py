Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(1,N-i+1):
            if S[j-1] != S[j+i-1]:
                l = j
        print(l)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l = j+1
        print(l)

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        l = 0
        for j in range(N-i):
            if S[j] != S[j+i]:
                l = j+1
            else:
                break
        print(l)
main()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    for i in range(1, n):
        l = 0
        for j in range(n-i):
            if s[j] != s[j+i]:
                l += 1
            else:
                break
        print(l)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    for i in range(1,N):
        for j in range(N-i):
            if S[j] == S[j+i]:
                print(j)
                break
        else:
            print(N-i)
    return

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        ans = 0
        for j in range(i):
            if S[j] != S[j + i]:
                ans += 1
        print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    for i in range(n-1):
        l = 0
        for j in range(1, n-i):
            if s[i] != s[i+j]:
                l = j
        print(l)

=======
Suggestion 9

def main():
    N = int(input())  # 2 ≦ N ≦ 5000
    S = input()  # 英小文字からなる長さ N の文字列
    # print(N)
    # print(S)

    # 1 ≦ i ≦ N-1
    for i in range(1, N):
        # print("i: ", i)
        # print("S[i]: ", S[i])
        # print("S[i-1]: ", S[i-1])
        # print("S[i+i]: ", S[i+i])
        # print("S[i+i-1]: ", S[i+i-1])
        # print("S[i+i-2]: ", S[i+i-2])
        # print("S[i+i-3]: ", S[i+i-3])
        # print("S[i+i-4]: ", S[i+i-4])
        # print("S[i+i-5]: ", S[i+i-5])
        # print("S[i+i-6]: ", S[i+i-6])
        # print("S[i+i-7]: ", S[i+i-7])
        # print("S[i+i-8]: ", S[i+i-8])
        # print("S[i+i-9]: ", S[i+i-9])
        # print("S[i+i-10]: ", S[i+i-10])
        # print("S[i+i-11]: ", S[i+i-11])
        # print("S[i+i-12]: ", S[i+i-12])
        # print("S[i+i-13]: ", S[i+i-13])
        # print("S[i+i-14]: ", S[i+i-14])
        # print("S[i+i-15]: ", S[i+i-15])
        # print("S[i+i-16]: ", S[i+i-16])
        # print("S[i+i-17]: ", S[i+i-17])
        # print("S[i+i-18]: ", S[i+i-18])
        # print("S[i+i-19]: ", S[i+i-19])
        # print("S[i+i-20]: ", S[i+i-20])
        # print("S[i+i-21]: ", S[i+i-21])
        # print("S[i+i-22]: ", S[i+i-22])
        #

=======
Suggestion 10

def main():
    N = int(input())
    S = input()
    for i in range(1, N):
        #print(i)
        result = 0
        for j in range(1, N - i + 1):
            if S[j - 1] != S[j + i - 1]:
                result += 1
            else:
                break
        print(result)
