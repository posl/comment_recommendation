def main():
    k = int(input())
    ans = 1
    for i in range(2, k):
        ans *= i
        if ans % k == 0:
            print(i)
            break
    else:
        print(k)
