def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if int(str(i)[-1]) == int(str(j)[0]) and int(str(i)[0]) == int(str(j)[-1]):
                cnt += 1
    print(cnt)
