def main():
    n = int(input())
    count = 0
    for i in range(1,n+1):
        if i < 10:
            count += 1
        elif i < 100:
            if i % 11 == 0:
                count += 1
        else:
            if i % 11 == 0:
                count += 2
    print(count)
