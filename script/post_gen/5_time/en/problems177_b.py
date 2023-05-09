Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        count = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
        if count < min:
            min = count
    print(min)

=======
Suggestion 2

def main():
    S = input()
    T = input()
    min = len(T)
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if min > count:
            min = count
    print(min)

=======
Suggestion 3

def main():
    s = input()
    t = input()
    res = len(t)
    for i in range(len(s) - len(t) + 1):
        cnt = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                cnt += 1
        res = min(res, cnt)
    print(res)

=======
Suggestion 4

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s)-len(t)+1):
        count_temp = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count_temp += 1
        if count == 0:
            count = count_temp
        elif count > count_temp:
            count = count_temp
    print(count)

=======
Suggestion 5

def solve():
    s = input()
    t = input()
    min = len(t)
    for i in range(len(s)-len(t)+1):
        c = 0
        for j in range(len(t)):
            if s[i+j] != t[j]:
                c += 1
        if c < min:
            min = c
    print(min)

solve()

=======
Suggestion 6

def main():
    s = input()
    t = input()
    count = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] != t:
            count += 1
    print(count)

=======
Suggestion 7

def find_min_changes(s, t):
    min_changes = len(s)
    for i in range(len(s) - len(t) + 1):
        changes = 0
        for j in range(len(t)):
            if s[i + j] != t[j]:
                changes += 1
        if changes < min_changes:
            min_changes = changes
    return min_changes

=======
Suggestion 8

def check(s,t):
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            return True
    return False

s = input()
t = input()
ans = len(t)
for i in range(len(s)-len(t)+1):
    if check(s[i:i+len(t)],t):
        ans = min(ans,len(t)-sum([1 for j in range(len(t)) if s[i+j] == t[j]]))
print(ans)

=======
Suggestion 9

def main():
    s = input()
    t = input()
    print(min([len(s) - i for i in range(len(t)) if s[i:i+len(t)] == t]))

=======
Suggestion 10

def main():
    S = raw_input()
    T = raw_input()
    #print S, T
    min_change = 1000
    for i in range(len(S)-len(T)+1):
        #print S[i:i+len(T)]
        change = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                change += 1
        if min_change > change:
            min_change = change
    print min_change
