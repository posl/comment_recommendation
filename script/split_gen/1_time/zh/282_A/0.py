def main():
    k = int(input())
    # print(k)
    # print(type(k))
    if k >= 1 and k <= 26:
        for i in range(0,k):
            print(chr(65+i),end="")
        print()
    else:
        print("K is out of range.")
        return 0
