def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        while t > 0:
            if S[k-1] == "A":
                if t % 3 == 1:
                    print("A")
                    break
                elif t % 3 == 2:
                    print("B")
                    break
                elif t % 3 == 0:
                    print("C")
                    break
            elif S[k-1] == "B":
                if t % 3 == 1:
                    print("B")
                    break
                elif t % 3 == 2:
                    print("C")
                    break
                elif t % 3 == 0:
                    print("A")
                    break
            elif S[k-1] == "C":
                if t % 3 == 1:
                    print("C")
                    break
                elif t % 3 == 2:
                    print("A")
                    break
                elif t % 3 == 0:
                    print("B")
                    break
            t -= 1
