def main():
    K = int(input())
    if K%2 == 0 or K%5 == 0:
        print(-1)
        return
    count = 1
    num = 7
    while num%K != 0:
        num = (num*10 + 7)%K
        count += 1
    print(count)
