def main():
    order = input()
    num = int(input())
    names = []
    for i in range(num):
        names.append(input())
    #print(order)
    #print(names)
    order_dict = {}
    for i in range(len(order)):
        order_dict[order[i]] = i
    #print(order_dict)
    names = sorted(names, key=lambda x: [order_dict[c] for c in x])
    for i in range(num):
        print(names[i])
