Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            break

=======
Suggestion 3

def main():
    n = int(input())
    s = input()

    for i in range(n):
        if s[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
            else:
                print('Aoki')
            return

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                print("Takahashi")
                return
            else:
                print("Aoki")
                return

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    print('Takahashi' if S.find('1') % 2 == 0 else 'Aoki')

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    print("Takahashi" if S.find("1") % 2 == 0 else "Aoki")

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if S[0] == '1':
        print('Aoki')
    else:
        print('Takahashi')

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    print("Takahashi" if s.find("1")%2 == 0 else "Aoki")

=======
Suggestion 9

def main():
    N = int(input())
    S = input()

    #print("N", N)
    #print("S", S)

    #print("S[0]", S[0])
    #print("S[1]", S[1])

    #print("S[1] == '1'", S[1] == '1')

    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break
