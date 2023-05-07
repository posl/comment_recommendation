def main():
    N = input()
    lenN = len(N)
    if lenN == 2:
        print(int(N))
        return
    if lenN == 3:
        print(max(int(N[0]) * int(N[1:]), int(N[:2]) * int(N[2:])))
        return
    if lenN == 4:
        print(max(int(N[0]) * int(N[1:]) , int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:])))
        return
    if lenN == 5:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:])))
        return
    if lenN == 6:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:])))
        return
    if lenN == 7:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:]), int(N[0:6]) * int(N[6:])))
        return
    if lenN == 8:
        print(max(int(N[0]) * int(N[1:]), int(N[0:2]) * int(N[2:]), int(N[0:3]) * int(N[3:]), int(N[0:4]) * int(N[4:]), int(N[0:5]) * int(N[5:]), int(N[0:6]) * int(N[6:]), int(N[0:7]) * int(N[7:])))
        return
    if lenN == 9:
        print(max(int(N[0]) * int(N[1:
