def main():
    N = int(input())
    c = input()
    count = 0
    #先把白色石头移到最右边
    for i in range(N):
        if c[i] == 'W':
            count += 1
    print(count)
    return 0
