def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if str(i)[-1] == str(j)[0] and str(i)[0] == str(j)[-1]:
                cnt += 1
    print(cnt)
