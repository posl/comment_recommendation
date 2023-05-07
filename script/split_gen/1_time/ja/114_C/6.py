def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if "3" in str(i) and "5" in str(i) and "7" in str(i):
            cnt += 1
    print(cnt)
