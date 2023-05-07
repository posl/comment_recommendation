def main():
    N = input()
    N = [int(i) for i in N]
    if sum(N)%9 == 0:
        print("Yes")
    else:
        print("No")
