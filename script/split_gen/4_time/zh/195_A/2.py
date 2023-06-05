def main():
    M,H = input().split()
    M = int(M)
    H = int(H)
    if H % M == 0:
        print("Yes")
    else:
        print("No")
