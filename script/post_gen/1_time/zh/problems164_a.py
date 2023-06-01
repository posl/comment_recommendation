Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def sheep_wolf(sheep,wolf):
    if wolf >= sheep:
        print("不安全")
    else:
        print("安全")

sheep,wolf = map(int,input().split())
sheep_wolf(sheep,wolf)

=======
Suggestion 2

def main():
    S, W = map(int, input().split())
    if S > W:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 3

def main():
    s, w = map(int, input().split())
    if w >= s:
        print("unsafe")
    else:
        print("safe")

=======
Suggestion 4

def main():
	# get input
	sheep, wolf = map(int, input().split())

	# judge
	if wolf >= sheep:
		print("不安全")
	else:
		print("安全")

=======
Suggestion 5

def main():
    sheep,wolf = map(int,input().split())
    if wolf >= sheep:
        print('不安全')
    else:
        print('安全')

=======
Suggestion 6

def main():
    line = input()
    S,W = line.split()
    S = int(S)
    W = int(W)
    if S > W:
        print("安全")
    else:
        print("不安全")

=======
Suggestion 7

def main():
    s,w = map(int, input().split())
    if s > w:
        print("安全")
    else:
        print("不安全")
