Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    h = list(map(int, input().split()))
    print(h.index(max(h))+1)

=======
Suggestion 2

def highest_bridge(N, H):
    highest = H[0]
    highest_index = 0
    for i in range(1, N):
        if H[i] > highest:
            highest = H[i]
            highest_index = i
    return highest_index + 1

N = int(input())
H = list(map(int, input().split()))
print(highest_bridge(N, H))

=======
Suggestion 3

def main():
    N = int(input())
    H = input().split()
    H = list(map(int, H))
    print(H.index(max(H))+1)

=======
Suggestion 4

def main():
    # Get the number of bridges
    num_bridges = int(input())

    # Get the heights of the bridges
    bridge_heights = list(map(int, input().split()))

    # Print the number of the highest bridge
    print(bridge_heights.index(max(bridge_heights)) + 1)

=======
Suggestion 5

def get_input():
    n = int(input())
    heights = [int(x) for x in input().split()]
    return n, heights

=======
Suggestion 6

def solve(N, H):
    return H.index(max(H))+1
