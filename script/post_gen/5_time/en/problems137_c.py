Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        s = input()
        s = ''.join(sorted(s))
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    d = {}
    for s in S:
        key = ''.join(sorted(s))
        d[key] = d.get(key, 0) + 1

    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2

    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    S = [input() for _ in range(N)]

    d = {}
    for s in S:
        ss = ''.join(sorted(s))
        if ss not in d:
            d[ss] = 1
        else:
            d[ss] += 1

    ans = 0
    for k in d:
        ans += d[k] * (d[k] - 1) // 2
    print(ans)

=======
Suggestion 4

def get_anagram_count(input_list):
    anagram_count = 0
    for i in range(len(input_list)):
        for j in range(i+1,len(input_list)):
            if sorted(input_list[i]) == sorted(input_list[j]):
                anagram_count += 1
    return anagram_count

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    count = 0
    temp = 1
    for i in range(N-1):
        if S[i] == S[i+1]:
            temp += 1
        else:
            count += (temp*(temp-1))//2
            temp = 1
    count += (temp*(temp-1))//2
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = ["".join(sorted(i)) for i in s]
    s = sorted(s)
    ans = 0
    cnt = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            cnt += 1
        else:
            ans += (cnt+1)*cnt//2
            cnt = 0
    ans += (cnt+1)*cnt//2
    print(ans)

=======
Suggestion 7

def get_anagram_count(s):
    anagram_count = 0
    anagram_dict = {}
    for i in range(len(s)):
        sorted_s = ''.join(sorted(s[i]))
        if sorted_s in anagram_dict:
            anagram_count += anagram_dict[sorted_s]
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    return anagram_count

=======
Suggestion 8

def solve():
    N = int(input())
    s = [input() for _ in range(N)]
    s = list(map(lambda x: ''.join(sorted(x)), s))
    from collections import defaultdict
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    ans = 0
    for i in d.values():
        ans += i * (i - 1) // 2
    print(ans)

=======
Suggestion 9

def get_anagram_count(s):
    letter_count = [0] * 26
    for c in s:
        letter_count[ord(c) - ord('a')] += 1
    return tuple(letter_count)

N = int(input())
anagram_count = {}
for i in range(N):
    s = input()
    key = get_anagram_count(s)
    if key in anagram_count:
        anagram_count[key] += 1
    else:
        anagram_count[key] = 1

result = 0
for key in anagram_count:
    result += anagram_count[key] * (anagram_count[key] - 1) // 2
print(result)

=======
Suggestion 10

def count_anagram(s):
    from collections import Counter
    count = Counter(s)
    return count
