Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    s = s.replace('A', '1')
    s = s.replace('C', '2')
    s = s.replace('G', '3')
    s = s.replace('T', '4')
    l = s.split('5')
    ans = 0
    for i in l:
        ans = max(ans, len(i))
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == 'A' or i == 'C' or i == 'G' or i == 'T':
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

main()

=======
Suggestion 4

def main():
    s = input()
    max = 0
    count = 0
    for i in s:
        if i == "A" or i == "C" or i == "G" or i == "T":
            count += 1
        else:
            if count > max:
                max = count
            count = 0
    if count > max:
        max = count
    print(max)

main()

I'm trying to make a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.

I've been trying to create a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.

I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the result I want. I am not sure how to use the strptime() function.

I'm trying to create a program that will take a string of numbers and separate them into a list of lists. For example, if the string is "123456789" the output should be [[1,2,3],[4,5,6],[7,8,9]]. I know how to do this with a list comprehension but I'm having trouble doing it with a generator.

I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the result I want. I am not sure how to use the strptime() function.

I have a string like this: '2016-06-23 17:00:00' and I want to convert it into a datetime object. I have tried a few things, but I am not getting the

=======
Suggestion 5

def main():
    s = input()
    ans = 0
    tmp = 0
    for i in s:
        if i in 'ACGT':
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 0
    ans = max(ans, tmp)
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    result = 0
    count = 0
    for i in s:
        if i in "ACGT":
            count += 1
        else:
            count = 0
        result = max(result, count)
    print(result)

=======
Suggestion 7

def main():
    s = input()
    acgt = 'ACGT'
    max = 0
    count = 0
    for i in range(len(s)):
        if s[i] in acgt:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
    print(max)

=======
Suggestion 8

def main():
    S = input()
    l = 0
    m = 0
    for c in S:
        if c in "ACGT":
            l += 1
        else:
            l = 0
        m = max(m, l)
    print(m)

=======
Suggestion 9

def main():
    S = input()
    max = 0
    count = 0
    for c in S:
        if c in ('A', 'C', 'G', 'T'):
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)

=======
Suggestion 10

def main():
    s = input()
    len_s = len(s)
    max_len = 0
    for i in range(len_s):
        for j in range(i, len_s):
            if all(c in 'ATCG' for c in s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    print(max_len)

main()
