Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    T = input()
    if T in S:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    S = input()
    T = input()
    if T in S:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    s = input()
    t = input()
    if t in s:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        return
    if len(S) < len(T):
        print('No')
        return
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def main():
    s = input()
    t = input()
    if len(s) < len(t):
        print('No')
    else:
        for i in range(len(s) - len(t) + 1):
            if s[i:i + len(t)] == t:
                print('Yes')
                exit()
        print('No')

=======
Suggestion 6

def main():
    S = input()
    T = input()
    if S == T:
        print("Yes")
        return
    for i in range(len(S)-len(T)):
        if S[i:i+len(T)] == T:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    s = input()
    t = input()
    
    if s == t:
        print("Yes")
        return
    
    for i in range(len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 8

def main():
	# 文字列の入力
	S = input()
	T = input()
	# Sの先頭からTを探す
	if S.find(T) != -1:
		print("Yes")
	else:
		print("No")
