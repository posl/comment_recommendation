def max_sushi(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    # print(sushi)
    # print(sushi[:K])
    # print(sushi[K:])
    # print(len(set(sushi[:K])))
    # print(len(set(sushi[K:])))
    # print(len(set(sushi[K:]))**2)
    return sum([x[1] for x in sushi[:K]]) + len(set(sushi[:K]))**2

if __name__ == '__main__':
    max_sushi()