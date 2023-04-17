Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    S = input()
    T = input()
    if sorted(S) == sorted(T):
        print("Yes")
    else:
        print("No")

=======

def main():
    s = input()
    t = input()
    if sorted(s) == sorted(t):
        print("Yes")
    else:
        print("No")

=======

def main():
    S = input()
    T = input()
    s = set(S)
    t = set(T)
    if len(s) == len(t):
        print('Yes')
    else:
        print('No')

=======

def main():
    s = input()
    t = input()
    d = {}
    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                print("No")
                return
        else:
            d[s[i]] = t[i]
    print("Yes")

=======

def main():
    S = input()
    T = input()

    if sorted(S) == sorted(T):
        print('Yes')
    else:
        print('No')

=======

def main():
    S = input()
    T = input()
    if len(set(S)) == len(set(T)):
        print("Yes")
    else:
        print("No")

=======

def main():
    s = input()
    t = input()
    if len(set(s)) == len(set(t)):
        print("Yes")
    else:
        print("No")

=======

def main():
    s = input()
    t = input()
    s = sorted(s)
    t = sorted(t)
    if s == t:
        print('Yes')
    else:
        print('No')

=======

def main():
    S = input()
    T = input()
    #print(S, T)
    #print(len(S))
    #print(len(T))
    #print(S[0])
    #print(T[0])
    #print(S[1])
    #print(T[1])
    #print(S[2])
    #print(T[2])
    #print(S[3])
    #print(T[3])
    #print(S[4])
    #print(T[4])
    #print(S[5])
    #print(T[5])
    #print(S[6])
    #print(T[6])
    #print(S[7])
    #print(T[7])
    #print(S[8])
    #print(T[8])
    #print(S[9])
    #print(T[9])
    #print(S[10])
    #print(T[10])
    #print(S[11])
    #print(T[11])
    #print(S[12])
    #print(T[12])
    #print(S[13])
    #print(T[13])
    #print(S[14])
    #print(T[14])
    #print(S[15])
    #print(T[15])
    #print(S[16])
    #print(T[16])
    #print(S[17])
    #print(T[17])
    #print(S[18])
    #print(T[18])
    #print(S[19])
    #print(T[19])
    #print(S[20])
    #print(T[20])
    #print(S[21])
    #print(T[21])
    #print(S[22])
    #print(T[22])
    #print(S[23])
    #print(T[23])
    #print(S[24])
    #print(T[24])
    #print(S[25])
    #print(T[25])
    #print(S[26])
    #print(T[26])
    #print(S[27])
    #print(T[27])
    #print(S[28])
    #print(T[28])
    #print(S[29])
    #print(T[29])
    #print(S[30])
    #print(T[30])
    #print(S[31])
    #print(T[31])
    #print(S[32])
    #print(T[32])
    #print(S[33])
