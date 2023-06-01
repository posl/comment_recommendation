Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h)) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    h = list(map(int, input().split()))
    max = h[0]
    for i in range(1, n):
        if max < h[i]:
            max = h[i]
    print(h.index(max)+1)

=======
Suggestion 3

def max_index(list):
    max = 0
    for i in range(1,len(list)):
        if list[i] > list[max]:
            max = i
    return max

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H))+1)

=======
Suggestion 5

def main():
    n = int(input())
    h = list(map(int, input().split()))

    max_index = 0
    for i in range(1, n):
        if h[i] > h[max_index]:
            max_index = i

    print(max_index + 1)

=======
Suggestion 6

def problem275_a():
    n = int(input())
    heights = list(map(int, input().split()))
    print(heights.index(max(heights)) + 1)

problem275_a()
