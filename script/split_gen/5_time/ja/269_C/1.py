def main():
    N = int(input())
    ans = []
    for i in range(1<<15):
        x = 0
        for j in range(15):
            if i & (1<<j):
                x += 2**j
        if x <= N:
            ans.append(x)
    print(*ans, sep="\n")
