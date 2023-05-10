def solve(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    eaten = []
    eaten_type = set()
    for i in range(K):
        eaten.append(sushi[i])
        eaten_type.add(sushi[i][0])
    eaten.sort(key=lambda x: x[0])
    result = sum([x[1] for x in eaten]) + len(eaten_type)**2
    for i in range(K, N):
        if sushi[i][0] not in eaten_type:
            eaten.append(sushi[i])
            eaten_type.add(sushi[i][0])
            eaten.sort(key=lambda x: x[0])
            result = max(result, sum([x[1] for x in eaten]) + len(eaten_type)**2)
    return result
