def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 200
    modA = [a % mod for a in A]
    modA2 = [[i, a] for i, a in enumerate(modA)]
    modA2.sort(key=lambda x: x[1])
    modA3 = []
    for i in range(len(modA2) - 1):
        if modA2[i][1] == modA2[i + 1][1]:
            modA3.append([modA2[i], modA2[i + 1]])
    if len(modA3) == 0:
        print("No")
        return
    else:
        print("Yes")
        print(2, modA3[0][0][0] + 1, modA3[0][1][0] + 1)
        print(1, modA3[0][0][0] + 1)
        return
