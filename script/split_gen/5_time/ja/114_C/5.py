def main():
    N = input()
    cnt = 0
    for i in range(3, len(N)+1):
        for j in range(len(N)+1-i):
            if int(N[j:j+i])%3 == 0:
                cnt += 1
    print(cnt)
