def main():
    n = input()
    k = len(n)
    if k == 1:
        if int(n) % 3 == 0:
            print(0)
        else:
            print(-1)
    else:
        n = list(n)
        n.sort()
        n.reverse()
        j = 0
        while j < k:
            s = 0
            for i in range(0, k):
                if i != j:
                    s += int(n[i])
            if s % 3 == 0:
                print(k - 1)
                break
            j += 1
        else:
            print(-1)
