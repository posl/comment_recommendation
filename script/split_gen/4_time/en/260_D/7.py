def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    #print(N, K, P)
    table = []
    for i in range(N):
        table.append(-1)
    for i in range(N):
        #print(table)
        card = P[i]
        #print("card:", card)
        if card == 1:
            table[0] = 1
            continue
        if table[card-2] == -1:
            table[card-1] = card
            continue
        if table[card-2] == card-1:
            table[card-1] = card
            continue
        if table[card-2] != card-1:
            table[card-1] = table[card-2]
            table[card-2] = -1
            continue
    for i in range(N):
        print(table[i])
