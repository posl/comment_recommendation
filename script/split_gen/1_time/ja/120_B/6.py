def main():
    A, B, K = map(int, input().split())
    divisor_list = []
    for i in range(1, 101):
        if A % i == 0 and B % i == 0:
            divisor_list.append(i)
    print(divisor_list[-K])
