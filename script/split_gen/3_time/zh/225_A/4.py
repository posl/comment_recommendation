def main():
    S = input()
    l = list(S)
    l1 = []
    for i in range(len(l)):
        if l[i] not in l1:
            l1.append(l[i])
    print(len(l1))
