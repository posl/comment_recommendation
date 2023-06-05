Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 2

def find_max_bridge(bridge_list):
    max_bridge = 0
    for i in range(len(bridge_list)):
        if bridge_list[i] > max_bridge:
            max_bridge = bridge_list[i]
    return max_bridge

=======
Suggestion 3

def main():
    N = int(input())
    H = list(map(int, input().split()))
    print(H.index(max(H)) + 1)

=======
Suggestion 4

def main():
    n = int(input())
    h = [int(x) for x in input().split()]
    print(h.index(max(h))+1)

=======
Suggestion 5

def main():
    n = int(input())
    h = [int(i) for i in input().split()]
    print(h.index(max(h))+1)

=======
Suggestion 6

def problems275_a():
    n = int(input())
    H = list(map(int, input().split()))
    maxH = max(H)
    for i in range(n):
        if H[i] == maxH:
            print(i+1)
            break

=======
Suggestion 7

def main():
    n = int(input())
    h = list(map(int, input().split()))
    h_max = max(h)
    for i in range(n):
        if h[i] == h_max:
            print(i + 1)
            break
