Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    for i in range(n):
        if s[i] == 'L':
            ans[i - 1] += (n - i + 1) // 2
            ans[i] += (n - i) // 2
        else:
            ans[i + 1] += (i + 2) // 2
            ans[i] += (i + 1) // 2
    print(' '.join(map(str, ans)))

=======
Suggestion 2

def main():
    s = input()
    s = s.replace('RL','R L')
    s = s.split(' ')
    ans = []
    for i in range(len(s)):
        ans.append(0)
    for i in range(len(s)):
        if s[i] == 'R':
            ans[i+1] += 1
        else:
            ans[i-1] += 1
    print(' '.join(map(str,ans)))

=======
Suggestion 3

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N-1):
        if S[i] == 'R':
            if S[i+1] == 'R':
                ans[i+1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i+1] += ans[i]
    for i in range(N-1, 0, -1):
        if S[i] == 'L':
            if S[i-1] == 'L':
                ans[i-1] += ans[i] + 1
                ans[i] = 0
        else:
            ans[i-1] += ans[i]
    print(' '.join(map(str, ans)))

main()

=======
Suggestion 4

def main():
    input_str = input()
    input_len = len(input_str)
    output_list = [0] * input_len
    
    #print(input_str)
    #print(input_len)
    #print(output_list)
    
    #print(input_str[0])
    #print(input_str[1])
    #print(input_str[2])
    
    #print(input_str[input_len-3])
    #print(input_str[input_len-2])
    #print(input_str[input_len-1])
    
    for i in range(input_len):
        #print(i)
        if input_str[i] == 'R':
            for j in range(i+1,input_len):
                if input_str[j] == 'L':
                    output_list[j-1] += 1
                    break
        elif input_str[i] == 'L':
            for j in range(i,0,-1):
                if input_str[j-1] == 'R':
                    output_list[j] += 1
                    break
        else:
            print('error')
    
    #print(output_list)
    
    for i in range(input_len):
        print(output_list[i],end=' ')

=======
Suggestion 5

def main():
    s = input()
    n = len(s)
    ans = [0] * n
    l = 0
    r = 0
    for i in range(n):
        if s[i] == 'L':
            l = i
        else:
            r = i
        if s[i] == 'R':
            ans[r] += 1
        else:
            ans[l] += 1
    print(' '.join(map(str, ans)))

=======
Suggestion 6

def solve():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            for j in range(i + 1, N):
                if S[j] == 'L':
                    if (j - i) % 2 == 0:
                        ans[j] += 1
                    else:
                        ans[j - 1] += 1
                    break
        else:
            for j in range(i - 1, -1, -1):
                if S[j] == 'R':
                    if (i - j) % 2 == 0:
                        ans[j] += 1
                    else:
                        ans[j + 1] += 1
                    break
    print(' '.join(map(str, ans)))

=======
Suggestion 7

def main():
    s = input()
    n = len(s)
    ans = [0]*n
    cnt = 0
    for i in range(n):
        if s[i] == 'R':
            cnt += 1
        else:
            ans[i] += cnt // 2 + (cnt + 1) // 2
            ans[i - 1] += cnt // 2
            cnt = 0
    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            cnt += 1
        else:
            ans[i] += cnt // 2 + (cnt + 1) // 2
            ans[i + 1] += cnt // 2
            cnt = 0
    print(' '.join(map(str, ans)))

=======
Suggestion 8

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N-1):
        if S[i] == 'R' and S[i+1] == 'L':
            ans[i] += 1
            ans[i+1] += 1
    for i in range(N):
        if S[i] == 'R':
            if ans[i] % 2 == 0:
                ans[i+1] += ans[i] // 2
                ans[i] = 0
            else:
                ans[i+1] += ans[i] // 2
                ans[i] = 1
        else:
            if ans[i] % 2 == 0:
                ans[i-1] += ans[i] // 2
                ans[i] = 0
            else:
                ans[i-1] += ans[i] // 2
                ans[i] = 1
    print(" ".join(map(str, ans)))

=======
Suggestion 9

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            if S[i+1] == 'L':
                if (i+1) % 2 == 0:
                    ans[i] += 1
                else:
                    ans[i+1] += 1
            else:
                if (i+1) % 2 == 0:
                    ans[i] += 1
                else:
                    ans[i+1] += 1
    print(*ans)

=======
Suggestion 10

def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == 'R':
            # Rの左側にいる人数
            ans[i+1] += ans[i]
            ans[i] = 0
        else:
            # Lの右側にいる人数
            ans[i-1] += ans[i]
            ans[i] = 0
    print(' '.join([str(x) for x in ans]))
