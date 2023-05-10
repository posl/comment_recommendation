def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = min(A, B, C, D, E)
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass
    if min_time == A or min_time == B or min_time == C or min_time == D:
        min_time = min_time + 10
    else:
        pass
    print(min_time)

if __name__ == '__main__':
    main()