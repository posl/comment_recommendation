def main():
    S = input()
    ans = 0
    for i in range(10000):
        x = str(i).zfill(4)
        flag = True
        for j in range(10):
            if S[j] == 'o' and str(j) not in x:
                flag = False
                break
            if S[j] == 'x' and str(j) in x:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
