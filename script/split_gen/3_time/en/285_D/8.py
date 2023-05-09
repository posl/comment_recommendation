def check(orders):
    for i in range(len(orders)-1):
        if orders[i][1] != orders[i+1][0]:
            return False
    return True
n = int(input())
orders = []
for i in range(n):
    orders.append(input().split())
orders.sort()
