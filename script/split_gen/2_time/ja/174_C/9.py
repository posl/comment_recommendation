def main():
    K = int(input())
    if K % 2 == 0 or K % 5 == 0:
        print(-1)
        return
    else:
        i = 1
        while i * 7 % K != 0:
            i += 1
        print(i)
