Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    print(len(set(s)))

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    print(len(set(S)))

main()

=======
Suggestion 3

def count_words(words):
    #print(words)
    words_list = words.split()
    #print(words_list)
    return len(set(words_list))

=======
Suggestion 4

def unique(l):
    return list(set(l))

N = int(input())
S = [input() for i in range(N)]
print(len(unique(S)))

=======
Suggestion 5

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    print(len(s))
