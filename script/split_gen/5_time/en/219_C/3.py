def main():
    new_order = input()
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    new_order_dict = {}
    for i in range(26):
        new_order_dict[new_order[i]] = chr(ord('a')+i)
    for i in range(n):
        s = ''
        for j in range(len(names[i])):
            s += new_order_dict[names[i][j]]
        names[i] = s
    names.sort()
    for i in range(n):
        s = ''
        for j in range(len(names[i])):
            s += new_order[new_order_dict[names[i][j]]]
        names[i] = s
    for i in range(n):
        print(names[i])
