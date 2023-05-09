def main():
    A, B, K = map(int, input().split())
    cnt = 0
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            cnt += 1
            if cnt == K:
                print(i)
                exit()
