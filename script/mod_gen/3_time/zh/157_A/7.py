def get_paper_num(N):
    if N%2 == 0:
        return N/2
    else:
        return (N+1)/2

if __name__ == '__main__':
    get_paper_num()