def dice_sum(a,b,c):
    return 21-a-b-c
a,b,c = map(int,input().split())
print(dice_sum(a,b,c))
