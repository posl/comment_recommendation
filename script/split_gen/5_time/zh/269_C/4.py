def main():
    N = int(input())
    # print(N)
    # print(bin(N))
    # print(len(bin(N)))
    # print(bin(2**60))
    # print(len(bin(2**60)))
    # print(bin(2**60).count('1'))
    # print(bin(N).count('1'))
    # print(bin(N).count('1') <= 15)
    result = []
    for i in range(0, 2**60):
        if bin(i).count('1') <= 15:
            if bin(i) in bin(N):
                result.append(i)
    # print(result)
    for j in result:
        print(j)
