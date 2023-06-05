def get_time():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    time = [A,B,C,D,E]
    min_time = min(time)
    if min_time%10 == 0:
        return min_time
    else:
        return (10 - min_time%10 + min_time)
