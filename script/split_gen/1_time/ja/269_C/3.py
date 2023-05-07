def main():
    N = int(input())
    keta = len(bin(N))-2
    for i in range(2**keta):
        if i & N == i:
            print(i)
