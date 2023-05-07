def main():
    n = int(input())
    b = bin(n)[2:]
    l = len(b)
    ans = []
    for i in range(2**l):
        s = bin(i)[2:].zfill(l)
        if all([s[j] == '0' or b[j] == '1' for j in range(l)]):
            ans.append(i)
    for i in ans:
        print(i)
