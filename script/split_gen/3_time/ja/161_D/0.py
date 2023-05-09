def main():
    K = int(input())
    if K <= 9:
        print(K)
    elif K <= 18:
        print(str(K - 9) + str(K - 9))
    elif K <= 27:
        print(str(K - 18) + str(K - 18) + str(K - 18))
    elif K <= 36:
        print(str(K - 27) + str(K - 27) + str(K - 27) + str(K - 27))
    elif K <= 45:
        print(str(K - 36) + str(K - 36) + str(K - 36) + str(K - 36) +
