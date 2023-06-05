def get_result(data, k):
    if k > data[-1]:
        return k + len(data)
    else:
        for i in range(len(data)):
            if k <= data[i]:
                return data[i] + 1
