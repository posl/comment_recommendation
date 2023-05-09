def main():
    K = int(input())
    print("{:02d}:{:02d}".format((K + 21) // 60 % 24, (K + 21) % 60))
