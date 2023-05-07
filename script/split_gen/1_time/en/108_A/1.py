def main():
    K = int(input())
    even = K // 2
    odd = K // 2 + K % 2
    print(even * odd)
