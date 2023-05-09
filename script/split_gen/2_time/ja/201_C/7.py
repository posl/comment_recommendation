def main():
    S = list(input())
    ans = 0
    for i in range(10000):
        if len(set(str(i))) != 4:
            continue
        flag = True
        for j in range(4):
            if S[int(str(i)[j])] == 'o' and str(i)[j] not in str(i):
                flag = False
                break
            if S[int(str(i)[j])] == 'x' and str(i)[j] in str(i):
                flag = False
                break
        if flag:
            ans += 1
    print(ans)
