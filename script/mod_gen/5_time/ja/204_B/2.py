def harvest_fruits(fruits):
    harvest = 0
    for fruit in fruits:
        if fruit > 10:
            harvest += fruit - 10
    return harvest
N = int(input())
A = list(map(int, input().split()))
print(harvest_fruits(A))
