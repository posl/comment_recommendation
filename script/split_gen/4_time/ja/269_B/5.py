def main():
    S = [input() for i in range(10)]
    ans = []
    for i in range(10):
        for j in range(10):
            if S[i][j] == '#':
                ans.append([i+1,j+1])
    print(ans[0][0],ans[0][1])
    print(ans[-1][0],ans[-1][1])
