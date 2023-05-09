def main():
    N = int(input())
    if N == 3:
        print("Yes")
        return
    tree = [0]*N
    for i in range(N-1):
        a,b = map(int, input().split())
        tree[a-1] += 1
        tree[b-1] += 1
    if tree.count(1) == 1:
        print("Yes")
    else:
        print("No")
