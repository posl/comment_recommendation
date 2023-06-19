def main():
    a = int(input())
    x = 7
    for i in range(1, a+1):
        if x % a == 0:
            print(i)
            break
        x = x*10 + 7
    else:
        print(-1)
