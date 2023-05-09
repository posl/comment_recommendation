def main():
    N = int(input())
    doublets = 0
    for i in range(N):
        dice = input().split()
        if dice[0] == dice[1]:
            doublets += 1
        else:
            doublets = 0
        if doublets == 3:
            print("Yes")
            exit()
    print("No")
