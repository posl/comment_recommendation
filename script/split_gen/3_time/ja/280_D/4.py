def main():
    k = int(input())
    n = 1
    for i in range(2, k):
        n *= i
        if n%k==0:
            print(i)
            break
