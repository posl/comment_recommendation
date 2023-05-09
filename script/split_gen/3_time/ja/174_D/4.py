def main():
    n = int(input())
    c = input()
    cnt = 0
    for i in range(n):
        if c[i] == 'R':
            cnt += 1
    print(cnt)
