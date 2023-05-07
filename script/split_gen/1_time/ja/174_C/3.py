def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    i = 1
    while True:
        if i % K == 0:
            print(i)
            return
        i += 1
