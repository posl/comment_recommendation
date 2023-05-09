def main():
    K = int(input())
    if K % 2 == 0:
        print(-1)
        return
    else:
        i = 1
        while True:
            if int(str(7) * i) % K == 0:
                print(i)
                return
            else:
                i += 1
