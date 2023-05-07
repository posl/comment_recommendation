def main():
    K = int(input())
    if K%2 == 0:
        print(-1)
        return
    i = 1
    tmp = 7%K
    while tmp != 0:
        tmp = (tmp*10 + 7)%K
        i += 1
    print(i)
