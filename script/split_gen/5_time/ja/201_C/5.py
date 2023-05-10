def main():
    S = input()
    o_count = S.count('o')
    x_count = S.count('x')
    q_count = S.count('?')
    if o_count > 4:
        print(0)
    elif o_count == 4:
        print(24)
    elif o_count == 3:
        print(36)
    elif o_count == 2:
        print(14+12*q_count)
    elif o_count == 1:
        print(1+12*q_count+6*q_count*(q_count-1))
    elif o_count == 0:
        print(q_count*(q_count-1)*(q_count-2)*(q_count-3))
    else:
        print(0)
