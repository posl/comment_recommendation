def main():
    k = int(input())
    a = 1
    for i in range(1,k+1):
        a *= i
        if a % k == 0:
            print(i)
            break
