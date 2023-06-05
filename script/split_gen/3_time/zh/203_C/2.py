def main():
    N,K = map(int,input().split())
    AB = []
    for i in range(N):
        A,B = map(int,input().split())
        AB.append([A,B])
    AB.sort()
    money = K
    for i in range(N):
        if money >= AB[i][0]:
            money += AB[i][1]
        else:
            print(money)
            break
    else:
        print(money)
