def main():
    n = int(input())
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        cnt += n // i - i + 1
    print(cnt)
