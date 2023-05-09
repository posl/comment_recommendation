Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 2

def missing_number(string):
    string = string.replace('0','')
    string = string.replace('1','')
    string = string.replace('2','')
    string = string.replace('3','')
    string = string.replace('4','')
    string = string.replace('5','')
    string = string.replace('6','')
    string = string.replace('7','')
    string = string.replace('8','')
    string = string.replace('9','')
    return string

=======
Suggestion 3

def solve():
    s = input()
    for i in range(1, 10):
        if not str(i) in s:
            print(i)
            return
solve()

=======
Suggestion 4

def missing_num(s):
    for i in range(10):
        if str(i) not in s:
            return i

=======
Suggestion 5

def find_missing_number(s):
    for i in range(1,10):
        if str(i) not in s:
            return i

=======
Suggestion 6

def missing_number(s):
    s = list(s)
    for i in range(10):
        if str(i) not in s:
            print(i)
            break

=======
Suggestion 7

def main():
    S = input()
    print(45 - sum([int(s) for s in S]))

=======
Suggestion 8

def main():
    #S = input()
    S = "023456789"
    #S = "459230781"
    S = list(S)
    S = [int(i) for i in S]
    S.sort()
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[len(S)-1])
    #print(S[len(S)-1]-S[0])
    for i in range(1,len(S)):
        if S[i]-S[i-1] != 1:
            print(S[i-1]+1)
            break
    else:
        print(S[len(S)-1]+1)
    return

=======
Suggestion 9

def main():
    S = input()
    print(45-sum(list(map(int, S))))
