def problem200_b(n,k):
    if k == 0:
        return n
    if n % 200 == 0:
        return problem200_b(n//200,k-1)
    else:
        return problem200_b(int(str(n)+"200"),k-1)

if __name__ == '__main__':
    problem200_b()