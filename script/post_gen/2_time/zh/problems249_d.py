Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    S = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count('1') != k:
            continue
        cnt = set()
        for j in range(n):
            if i >> j & 1:
                for c in S[j]:
                    cnt.add(c)
        if len(cnt) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 2

def solve():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count('1') != k:
            continue
        t = set()
        for j in range(n):
            if i >> j & 1:
                t |= set(s[j])
        if len(t) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)
solve()

=======
Suggestion 3

def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(2**N):
        T = []
        for j in range(N):
            if (i>>j)&1:
                T.append(S[j])
        if len(T)!=K:
            continue
        cnt = 0
        for j in range(26):
            flag = False
            for k in range(K):
                if chr(ord('a')+j) in T[k]:
                    flag = True
            if flag:
                cnt+=1
        if cnt==K:
            ans = max(ans,K)
    print(ans)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(1<<N):
        if bin(i).count("1") == K:
            tmp = set()
            for j in range(N):
                if i & (1<<j):
                    tmp |= set(S[j])
            if len(tmp) == K:
                ans = max(ans,bin(i).count("1"))
    print(ans)

=======
Suggestion 5

def get_ans(n, k, s):
    ans = 0
    for i in range(1<<n):
        if bin(i).count('1') != k:
            continue
        tmp = set()
        for j in range(n):
            if i & (1<<j):
                for c in s[j]:
                    tmp.add(c)
        if len(tmp) == k:
            ans = max(ans, bin(i).count('1'))
    return ans

=======
Suggestion 6

def compute():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count("1") != k:
            continue
        st = set()
        for j in range(n):
            if i >> j & 1:
                for c in s[j]:
                    st.add(c)
        if len(st) == k:
            ans = max(ans, bin(i).count("1"))
    print(ans)

compute()

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    S = [input() for i in range(N)]
    ans = 0
    for i in range(1 << N):
        if bin(i).count('1') != K:
            continue
        A = []
        for j in range(N):
            if (i >> j) & 1:
                A.append(S[j])
        C = set(''.join(A))
        if len(C) == K:
            ans = max(ans, len(C))
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(1 << n):
        if bin(i).count('1') != k:
            continue
        c = set()
        for j in range(n):
            if i >> j & 1:
                c |= set(s[j])
        if len(c) == k:
            ans = max(ans, bin(i).count('1'))
    print(ans)

=======
Suggestion 9

def get_max_num_of_alphabets(N, K, S):
    max_num = 0
    for i in range(1, 2**N):
        i_str = str(bin(i))[2:]
        i_str = i_str.zfill(N)
        #print("i_str = {}".format(i_str))
        num_of_alphabets = 0
        for j in range(N):
            if i_str[j] == '1':
                num_of_alphabets += len(S[j])
        if num_of_alphabets == K:
            num_of_alphabets = 0
            alphabets = []
            for j in range(N):
                if i_str[j] == '1':
                    for k in range(len(S[j])):
                        if S[j][k] not in alphabets:
                            alphabets.append(S[j][k])
                            num_of_alphabets += 1
            if num_of_alphabets == K:
                max_num = max(max_num, i_str.count('1'))
    return max_num

=======
Suggestion 10

def get_max_num_of_letters_in_K_strings(N, K, S):
    max_num_of_letters = 0
    for i in range(1, 2**N):
        num_of_letters = 0
        letters = set()
        for j in range(N):
            if (i >> j) & 1:
                num_of_letters += len(S[j])
                letters = letters.union(set(S[j]))
        if num_of_letters == K and len(letters) == K:
            max_num_of_letters = K
            break
        elif num_of_letters > max_num_of_letters and len(letters) == K:
            max_num_of_letters = num_of_letters
    return max_num_of_letters
