def main():
    N = int(input())
    ans = [0]
    for i in range(60):
        if N & 1<<i:
            ans.append(1<<i)
            for j in range(len(ans)-1):
                ans.append(ans[j]+ans[-1])
    ans.sort()
    for a in ans:
        print(a)
