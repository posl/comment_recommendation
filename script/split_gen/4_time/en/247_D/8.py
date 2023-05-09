def main():
    q = int(input())
    # print(q)
    c = []
    x = []
    for i in range(q):
        query = input().split()
        # print(query)
        if query[0] == '1':
            x.append(int(query[1]))
            c.append(int(query[2]))
        else:
            c_ = int(query[1])
            sum_ = 0
            for i in range(len(c)):
                if c_ > 0:
                    if c[i] <= c_:
                        sum_ += c[i] * x[i]
                        c_ -= c[i]
                        c[i] = 0
                    else:
                        sum_ += c_ * x[i]
                        c[i] -= c_
                        c_ = 0
            print(sum_)
