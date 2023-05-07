def main():
    P = input().split()
    P = [int(i) for i in P]
    P = [chr(i + 96) for i in P]
    print("".join(P))
