def main():
    N = int(input())
    node = [0] * N
    for i in range(N-1):
        a, b = map(int, input().split())
        node[a-1] += 1
        node[b-1] += 1
    if node.count(1) == 1:
        print("Yes")
    else:
        print("No")
