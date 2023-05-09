def main():
    x = list(map(int, input().split()))
    for i in range(1, 6):
        if x[i - 1] == 0:
            print(i)
            break
