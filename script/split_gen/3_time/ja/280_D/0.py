def main():
    k = int(input())
    n = 0
    for i in range(2, k+1):
        if k % i == 0:
            n = i
            break
    print(n)
