def is_sgs(x):
    x_str = str(x)
    return "7" in x_str and "5" in x_str and "3" in x_str
n = int(input())
sgs = 0
queue = [3, 5, 7]
while queue:
    x = queue.pop()
    if x > n:
        continue
    if is_sgs(x):
        sgs += 1
    queue.append(x * 10 + 3)
    queue.append(x * 10 + 5)
    queue.append(x * 10 + 7)
print(sgs)
