def dice_sum(A, B):
    if A * 1 > B or A * 6 < B:
        return 'No'
    else:
        return 'Yes'
A, B = map(int, input().split())
print(dice_sum(A, B))
