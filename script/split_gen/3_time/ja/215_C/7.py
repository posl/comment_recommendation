def main():
    S, K = input().split(" ")
    K = int(K)
    print("".join(sorted(S)[K-1]))
main()
