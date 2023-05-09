def main():
    Sx, Sy, Gx, Gy = input().split()
    Sx, Sy, Gx, Gy = int(Sx), int(Sy), int(Gx), int(Gy)
    print((Gx*Sy + Sx*Gy)/(Sy + Gy))
main()
