def main():
    n = int(input())
    n = bin(n)[2:]
    n = n[::-1]
    n = n.split("1")
    for i in range(len(n)):
        if n[i] != "":
            n[i] = (2**i)
    n = list(map(str,n))
    print(len(n))
    print(" ".join(n))
