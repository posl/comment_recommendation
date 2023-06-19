Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 2

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    print(h.index(max(h))+1)

=======
Suggestion 3

def main():
    N = int(input())
    H = [int(x) for x in input().split()]
    print(H.index(max(H))+1)

=======
Suggestion 4

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H))+1)

=======
Suggestion 5

def get_max_bridge(bridge_heights):
    max_height = 0
    max_index = 0
    for i in range(0, len(bridge_heights)):
        if bridge_heights[i] > max_height:
            max_height = bridge_heights[i]
            max_index = i + 1
    return max_index
