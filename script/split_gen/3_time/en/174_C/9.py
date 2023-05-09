def main():
    # input
    k = int(input())
    # solve
    if k % 2 == 0:
        print(-1)
    else:
        seven = 7
        for i in range(1, 10**6+1):
            if seven % k == 0:
                print(i)
                break
            else:
                seven = seven * 10 + 7
