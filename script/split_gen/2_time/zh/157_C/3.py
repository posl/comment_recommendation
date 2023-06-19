def main():
    while True:
        try:
            N, M = map(int, input().split())
            if N < 1 or N > 3 or M < 0 or M > 5:
                print(-1)
                continue
            num = [0] * N
            for i in range(M):
                s, c = map(int, input().split())
                if s < 1 or s > N or c < 0 or c > 9:
                    print(-1)
                    break
                num[s - 1] = c
            else:
                if N == 1:
                    if num[0] == 0:
                        print(0)
                    else:
                        print(num[0])
                elif N == 2:
                    if num[0] == 0:
                        print(-1)
                    else:
                        print(num[0] * 10 + num[1])
                elif N == 3:
                    if num[0] == 0 and num[1] == 0:
                        print(-1)
                    elif num[0] == 0 and num[1] != 0:
                        print(num[1] * 10 + num[2])
                    elif num[0] != 0 and num[1] == 0:
                        print(num[0] * 100 + num[2])
                    else:
                        print(num[0] * 100 + num[1] * 10 + num[2])
        except:
            break
