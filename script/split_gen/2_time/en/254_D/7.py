def main():
    n = int(input())
    count = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i*j == int(i**0.5)**2 * int(j**0.5)**2:
                if i == j:
                    count += 1
                else:
                    count += 2
    print(count)
