def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    order = [A,B,C,D,E]
    order.sort()
    #print(order)
    for i in range(5):
        if order[i] % 10 != 0:
            order[i] = order[i] + 10 - order[i] % 10
    #print(order)
    print(order[0]+order[1]+order[2]+order[3]+order[4])
