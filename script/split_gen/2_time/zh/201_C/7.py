def main():
    S = input()
    ans = 0
    for i in range(10000):
        flag = True
        for j in range(10):
            if S[j] == 'o' and str(i).find(str(j)) == -1:
                flag = False
            elif S[j] == 'x' and str(i).find(str(j)) != -1:
                flag = False
        if flag:
            ans += 1
    print(ans)
