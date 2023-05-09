def check(L):
    if max(L) < sum(L) - max(L):
        return 'Yes'
    else:
        return 'No'
N = int(input())
L = list(map(int, input().split()))
print(check(L))
