def find_parent(n, parent):
    if parent[n] == 1:
        return 1
    else:
        return find_parent(parent[n], parent) + 1
n = int(input())
parent = [1] + list(map(int, input().split()))
print(find_parent(n, parent))
