def get_depth(p, depth):
    if p == 1:
        return depth
    else:
        return get_depth(parents[p], depth+1)
N = int(input())
parents = list(map(int, input().split()))
depth = 0
for i in range(N):
    depth = max(depth, get_depth(i+1, 1))
print(depth)

if __name__ == '__main__':
    get_depth()