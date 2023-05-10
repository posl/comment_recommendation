def main():
    n = int(input())
    n = bin(n)
    n = n[2:]
    n = n[::-1]
    ans = [0]
    for i in range(len(n)):
        if n[i] == "1":
            for j in range(len(ans)):
                ans[j] += 2**i
        else:
            ans += ans
    ans.sort()
    for i in ans:
        print(i)
