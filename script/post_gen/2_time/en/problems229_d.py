Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    l = []
    count = 0
    for i in range(len(s)):
        if s[i] == 'X':
            count += 1
        else:
            l.append(count)
            count = 0
    l.append(count)
    if k >= len(l):
        print(len(s))
    else:
        print(max([sum(l[i:i+k+1]) for i in range(len(l)-k)]))

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if K > 0:
                K -= 1
                count += 1
            else:
                break
    print(count)

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    S = S.replace('.','0')
    S = S.replace('X','1')
    S = S.split('0')
    ans = 0
    for i in range(len(S)):
        if len(S[i]) > ans:
            ans = len(S[i])
    if ans > K:
        ans = K
    print(ans)

=======
Suggestion 4

def main():
    s = input()
    k = int(input())
    l = len(s)
    if l == 1:
        print(k//2)
        return
    if k == 0:
        print(s.count('X'))
        return
    if s[0] == 'X':
        i = 1
        while i < l and s[i] == 'X':
            i += 1
        if i == l:
            print(l*k//2)
            return
        ans = i//2
        i += 1
    else:
        ans = 0
        i = 0
    while i < l:
        j = i
        while j < l and s[j] == '.':
            j += 1
        ans += (j-i-1)//2
        i = j+1
    print(ans+k)

=======
Suggestion 5

def main():
    S = input()
    K = int(input())

    S = S.replace("..", ".")

    if K == 0:
        print(S.count("X"))
    else:
        S = S.replace(".", "X", K)
        print(S.count("X"))

main()

=======
Suggestion 6

def main():
    s = input()
    k = int(input())

    # Count consecutive Xs
    c = 0
    max_c = 0
    for i in range(len(s)):
        if s[i] == 'X':
            c += 1
        else:
            if max_c < c:
                max_c = c
            c = 0
    if max_c < c:
        max_c = c

    # Replace . with X
    if k > 0:
        # Count consecutive Xs after the first X
        c = 0
        for i in range(len(s)):
            if s[i] == 'X':
                c += 1
            else:
                break

        # Count consecutive Xs before the last X
        c2 = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == 'X':
                c2 += 1
            else:
                break

        # Count consecutive Xs between the first and last X
        c3 = 0
        for i in range(c, len(s) - c2):
            if s[i] == 'X':
                c3 += 1
            else:
                if max_c < c + k:
                    max_c = c + k
                c = 0
        if max_c < c + k:
            max_c = c + k

    print(max_c)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    S = S.replace('.', '')
    S = S.replace('X', ' ')
    S = S.split(' ')
    S = list(map(len, S))
    S = list(map(lambda x: x - 1, S))
    S = list(filter(lambda x: x > 0, S))
    S = list(map(lambda x: x - 1, S))
    S = list(filter(lambda x: x > 0, S))
    S = list(map(lambda x: x // 2, S))
    S = list(map(lambda x: x * 2, S))
    S = sum(S)
    if K > 0:
        S += 1
    print(S)

=======
Suggestion 8

def get_input():
    s = input()
    k = int(input())
    return s, k

=======
Suggestion 9

def problem():
    # input
    S = input()
    K = int(input())
    
    # initialization
    count = 0
    max_count = 0
    for i in range(len(S)):
        if S[i] == 'X':
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    
    # output
    print(max_count + K)

=======
Suggestion 10

def main():
    S = input()
    K = int(input())

    #print(S,K)
    #print(type(S),type(K))

    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])


    #print(S[0:3])
    #print(S[1:4])
    #print(S[2:5])
    #print(S[3:6])

    #print(S[0:4])
    #print(S[1:5])
    #print(S[2:6])
    #print(S[3:7])

    #print(S[0:5])
    #print(S[1:6])
    #print(S[2:7])
    #print(S[3:8])

    #print(S[0:6])
    #print(S[1:7])
    #print(S[2:8])
    #print(S[3:9])

    #print(S[0:7])
    #print(S[1:8])
    #print(S[2:9])
    #print(S[3:10])

    #print(S[0:8])
    #print(S[1:9])
    #print(S[2:10])
    #print(S[3:11])

    #print(S[0:9])
    #print(S[1:10])
    #print(S[2:11])
    #print(S[3:12])

    #print(S[0:10])
    #print(S[1:11])
    #print(S[2:12])
    #print(S[3:13])

    #print(S[0:11])
    #print(S[1:12])
    #print(S[2:13])
    #print(S[3:14])

    #print(S[0:12])
    #print(S[1:13])
    #print(S[2:14])
    #print(S[3:15])

    #print(S[0:13])
    #print(S[1:14])
    #print(S[2:15])
    #print(S[3:16])

    #print(S[0:14])
    #print(S[1:15])
    #print(S[2:16])
    #print(S[3:17])

    #print(S[0:15])
    #print
