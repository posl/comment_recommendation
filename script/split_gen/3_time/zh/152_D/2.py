def main():
    n = int(input())
    a = 0
    for i in range(1,n+1):
        if i < 10:
            a += 1
        elif i < 100:
            if i % 11 == 0:
                a += 1
        elif i < 1000:
            if i % 11 == 0:
                a += 2
        elif i < 10000:
            if i % 11 == 0:
                a += 3
        elif i < 100000:
            if i % 11 == 0:
                a += 4
        else:
            if i % 11 == 0:
                a += 5
    print(a)
