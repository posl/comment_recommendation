def main():
    N = int(input())
    for i in range(100):
        if 4*i <= N and (N - 4*i)%7 == 0:
            print("Yes")
            return
    print("No")
