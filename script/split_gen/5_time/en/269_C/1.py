def main():
    n = int(input())
    ans = []
    for i in range(1<<15):
        x = 0
        for j in range(15):
            if i & (1<<j):
                x |= 1<<(2*j)
        if x <= n and x > 0:
            ans.append(x)
    ans.sort()
    for i in ans:
        print(i)
