Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 2

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute
    ans = 1
    nums = [A, B, C, D, E]
    for i in range(5):
        for j in range(i+1, 5):
            if nums[i] == nums[j]:
                break
            elif j == 4:
                ans += 1

    # output
    print(ans)

=======
Suggestion 3

def main():
    a = input().split()
    print(len(set(a)))

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int, input().split())
    print(len(set([a,b,c,d,e])))

=======
Suggestion 5

def main():
    a,b,c,d,e = map(int, input().split())
    l = [a,b,c,d,e]
    print(len(set(l)))

=======
Suggestion 6

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    print(len(set([A, B, C, D, E])))
