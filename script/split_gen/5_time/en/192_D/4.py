def main():
    x = input()
    m = int(input())
    d = max([int(i) for i in x])
    l = len(x)
    if l == 1:
        print(1 if int(x) <= m else 0)
        return
    else:
        n = d + 1
        while True:
            t = 0
            for i in range(l):
                t += n ** (l - i - 1) * int(x[i])
                if t > m:
                    break
            if t > m:
                break
            n += 1
        print(n - d - 1)
