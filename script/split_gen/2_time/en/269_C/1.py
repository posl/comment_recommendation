def main():
    N = int(input())
    b = bin(N)[2:]
    b = b[::-1]
    for i in range(2**len(b)):
        c = bin(i)[2:]
        c = c[::-1]
        if len(c) < len(b):
            c += "0" * (len(b) - len(c))
        ans = 0
        for j in range(len(c)):
            if c[j] == "1" and b[j] == "1":
                ans += 2**j
        print(ans)
