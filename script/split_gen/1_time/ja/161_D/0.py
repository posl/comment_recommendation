def main():
    N = int(input())
    if N == 1:
        print(1)
        return
    if N == 2:
        print(2)
        return
    if N == 3:
        print(3)
        return
    N -= 3
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if abs(j - k) <= 1:
                    N -= 1
                    if N == 0:
                        print(str(i) + str(j) + str(k))
                        return
