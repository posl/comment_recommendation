def main():
    n = int(input())
    b = bin(n)[2:]
    b = '0'*(60-len(b)) + b
    b = b[::-1]
    pos = []
    for i in range(len(b)):
        if b[i] == '1':
            pos.append(i)
    for i in range(2**len(pos)):
        ans = 0
        for j in range(len(pos)):
            if (i >> j) & 1:
                ans += 2**pos[j]
        print(ans)
