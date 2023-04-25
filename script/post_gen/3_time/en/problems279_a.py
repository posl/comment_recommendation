Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(0, len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == "v":
            v += 1
        else:
            w += 1
    print(v * w)

=======
Suggestion 3

def main():
    s = input()
    v_count = 0
    w_count = 0
    bottom_count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v_count += 1
            bottom_count += w_count
        else:
            w_count += 1
    print(bottom_count)

=======
Suggestion 4

def main():
    s = input()
    count = 0
    for i in range(1,len(s)):
        if s[i] == 'v' and s[i-1] == 'v':
            count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            count += 1
    print(count*(count-1)//2)

=======
Suggestion 6

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "v":
            ans += len(s[i+1:]) - s[i+1:].count("v")
    print(ans)

=======
Suggestion 8

def getBottoms(s):
    bottoms = 0
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        elif s[i] == 'w':
            w += 1
        if v > w:
            bottoms += 1
    return bottoms

S = input()
print(getBottoms(S))

=======
Suggestion 9

def main():
    #get input
    s = input()
    #count number of bottoms
    count = 0
    for i in range(len(s)-1):
        if s[i] == "v" and s[i+1] == "v":
            count += 1
    #print result
    print(count)

main()

=======
Suggestion 10

def main():
    S = input()
    #print(S)
    #print(len(S))
    count = 0
    for i in range(0, len(S)):
        if S[i] == 'v':
            count += 1
    print(count * (count - 1) // 2)
