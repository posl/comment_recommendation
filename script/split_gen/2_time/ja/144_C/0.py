def main():
    N = int(input())
    cnt = 0
    i = 1
    while i < N:
        i += i
        cnt += 1
    print(cnt)
