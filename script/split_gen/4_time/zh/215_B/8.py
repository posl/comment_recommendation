def main():
    print("请输入一个正整数N，找出最大的整数k，使2^k≦N。")
    N = int(input())
    k = 0
    while (N >= 2):
        N = N/2
        k += 1
    print(k)
