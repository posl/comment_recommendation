def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        if s[i:i+3] == 'ABC':
            cnt += 1
    print(cnt)
