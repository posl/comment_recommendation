def main():
    P = int(input())
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    count = 0
    while P > 0:
        for i in range(10):
            if P >= coins[-1-i]:
                P = P - coins[-1-i]
                count = count + 1
                break
    print(count)
