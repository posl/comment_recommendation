def main():
    K = int(input())
    print(int("".join(["2" if i % 2 == 0 else "0" for i in range(K)])))
