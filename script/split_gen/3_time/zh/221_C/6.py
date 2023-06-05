def max_product(n):
    n = str(n)
    l = len(n)
    if l == 2:
        return int(n[0]) * int(n[1])
    elif l == 3:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]))
    elif l == 4:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]))
    elif l == 5:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]), int(n[3]) * int(n[4:]))
    elif l == 6:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]), int(n[3]) * int(n[4:]), int(n[4]) * int(n[5:]))
    elif l == 7:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]), int(n[3]) * int(n[4:]), int(n[4]) * int(n[5:]), int(n[5]) * int(n[6:]))
    elif l == 8:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]), int(n[3]) * int(n[4:]), int(n[4]) * int(n[5:]), int(n[5]) * int(n[6:]), int(n[6]) * int(n[7:]))
    elif l == 9:
        return max(int(n[0]) * int(n[1:]) , int(n[1]) * int(n[2:]), int(n[2]) * int(n[3:]), int(n[3]) * int(n[4:]), int(n[4]) * int(n[5:]), int(n[5]) * int(n[6
