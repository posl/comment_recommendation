def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(2**n):
        x = bin(i)[2:].zfill(n)
        y = x[0]
        for j in range(n):
            if s[j] == "AND":
                y = str(int(y) & int(x[j+1]))
            else:
                y = str(int(y) | int(x[j+1]))
        if y == "1":
            ans += 1
    print(ans)
