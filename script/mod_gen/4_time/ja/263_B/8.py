def count_parent(n,p):
    if p == 1:
        return 1
    else:
        return count_parent(n,p-1) + 1
n = int(input())
p = list(map(int,input().split()))
print(count_parent(n,p[-1]))
