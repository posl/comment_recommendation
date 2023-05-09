def main():
    s = [input() for _ in range(10)]
    ans = []
    for i in range(10):
        for j in range(10):
            if s[i][j] == "#":
                ans.append([i,j])
    print(ans[0][0]+1,ans[0][1]+1)
    print(ans[-1][0]+1,ans[-1][1]+1)
