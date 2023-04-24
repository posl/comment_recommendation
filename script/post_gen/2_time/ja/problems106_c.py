Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    S = S.replace("2","22")
    S = S.replace("3","333")
    S = S.replace("4","4444")
    S = S.replace("5","55555")
    S = S.replace("6","666666")
    S = S.replace("7","7777777")
    S = S.replace("8","88888888")
    S = S.replace("9","999999999")
    print(S[K-1])

=======
Suggestion 2

def main():
    S = input()
    K = int(input())
    S = S.replace('1', '1 ')
    S = S.replace('2', '2 22 ')
    S = S.replace('3', '3 333 ')
    S = S.replace('4', '4 4444 ')
    S = S.replace('5', '5 55555 ')
    S = S.replace('6', '6 666666 ')
    S = S.replace('7', '7 7777777 ')
    S = S.replace('8', '8 88888888 ')
    S = S.replace('9', '9 999999999 ')
    S = S.split()
    print(S[K-1])

=======
Suggestion 3

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            break
    else:
        print(1)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] == "1":
            continue
        else:
            print(S[i])
            break
    else:
        print(1)

=======
Suggestion 5

def main():
    S = input()
    K = int(input())
    for i in range(K):
        S = S.replace('1', '11')
        S = S.replace('2', '22')
        S = S.replace('3', '33')
        S = S.replace('4', '44')
        S = S.replace('5', '55')
        S = S.replace('6', '66')
        S = S.replace('7', '77')
        S = S.replace('8', '88')
        S = S.replace('9', '99')
        if len(S) >= K:
            break
    print(S[K-1])

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(K):
        if S[i] == '1':
            count += 1
        else:
            print(S[i])
            break
        if count == K:
            print(1)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != "1":
            print(S[i])
            break
    else:
        print("1")

=======
Suggestion 8

def main():
    s = input()
    k = int(input())
    i = 0
    for i in range(k):
        if s[i] != '1':
            break
    if i == k:
        print(1)
    else:
        print(s[i])

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    s = S
    i = 0
    while i < K:
        if len(s) > K:
            print(s[K-1])
            break
        s = s.replace('1', '11')
        s = s.replace('2', '22')
        s = s.replace('3', '33')
        s = s.replace('4', '44')
        s = s.replace('5', '55')
        s = s.replace('6', '66')
        s = s.replace('7', '77')
        s = s.replace('8', '88')
        s = s.replace('9', '99')
        i += 1
    else:
        print(s[K-1])

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    #print("S:", S)
    #print("K:", K)
    #print("len(S):", len(S))
    #print("type(S):", type(S))
    #print("type(K):", type(K))
    #print("S[0]:", S[0])
    #print("S[0:1]:", S[0:1])
    #print("S[0:2]:", S[0:2])
    #print("S[0:3]:", S[0:3])
    #print("S[0:4]:", S[0:4])
    #print("S[0:5]:", S[0:5])
    #print("S[0:6]:", S[0:6])
    #print("S[0:7]:", S[0:7])
    #print("S[0:8]:", S[0:8])
    #print("S[0:9]:", S[0:9])
    #print("S[0:10]:", S[0:10])
    #print("S[0:11]:", S[0:11])
    #print("S[0:12]:", S[0:12])
    #print("S[0:13]:", S[0:13])
    #print("S[0:14]:", S[0:14])
    #print("S[0:15]:", S[0:15])
    #print("S[0:16]:", S[0:16])
    #print("S[0:17]:", S[0:17])
    #print("S[0:18]:", S[0:18])
    #print("S[0:19]:", S[0:19])
    #print("S[0:20]:", S[0:20])
    #print("S[0:21]:", S[0:21])
    #print("S[0:22]:", S[0:22])
    #print("S[0:23]:", S[0:23])
    #print("S[0:24]:", S[0:24])
    #print("S[0:25]:", S[0:25])
