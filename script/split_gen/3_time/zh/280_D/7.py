def main():
    k = int(input())
    mod = 1
    for i in range(2, k + 1):
        mod *= i
        mod %= k
    print(k - mod)
