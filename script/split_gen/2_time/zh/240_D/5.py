def main():
    num = int(input())
    ball = list(map(int,input().split()))
    for i in range(num):
        if ball[i] % 2 == 0:
            print(1)
        else:
            print(0)
