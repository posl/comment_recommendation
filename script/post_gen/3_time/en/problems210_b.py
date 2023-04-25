Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == '1':
            if i % 2 == 0:
                print("Takahashi")
            else:
                print("Aoki")
            break

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    for i in range(N):
        if S[i] == "1":
            print("Takahashi" if i % 2 == 0 else "Aoki")
            break

=======
Suggestion 4

def main():
    N = int(input())
    S = input()
    print("Takahashi" if S.find("1") % 2 == 0 else "Aoki")

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    print('Takahashi' if s.find('1') % 2 == 0 else 'Aoki')

=======
Suggestion 6

def main():
    # input
    N = int(input())
    S = input()

    # compute
    if S.count('1') % 2 == 0:
        ans = 'Takahashi'
    else:
        ans = 'Aoki'

    # output
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    if S[0] == "0":
        print("Takahashi")
    elif S[0] == "1":
        if S.count("1") % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")

=======
Suggestion 8

def main():
    N = int(input())
    S = input()
    print("Takahashi" if S.find('1')%2 == 0 else "Aoki")

main()

=======
Suggestion 9

def main():
    # read input
    N = int(input())
    S = input()

    # solve problem
    ans = "Aoki"
    for i in range(N):
        if S[i] == "1":
            if i % 2 == 0:
                ans = "Takahashi"
            break

    # print answer
    print(ans)
