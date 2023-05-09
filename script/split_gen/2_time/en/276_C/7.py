def permute(a, b):
    if a == b:
        return
    else:
        for i in range(a, b):
            if permute(a, b-1) == False:
                return False
            if b % 2 == 0:
                a, b = i, b-1
            else:
                a, b = 0, b-1
            print(a, b)
        return True
permute(0, 9)
