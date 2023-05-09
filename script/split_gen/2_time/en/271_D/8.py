def cardSum(n, S, cards):
    if n == 1:
        if cards[0][0] == S or cards[0][1] == S:
            return True, [0]
        else:
            return False, None
    else:
        for i in range(2**n):
            mask = i
            sum = 0
            indices = []
            for j in range(n):
                if mask % 2 == 0:
                    sum += cards[j][0]
                    indices.append(0)
                else:
                    sum += cards[j][1]
                    indices.append(1)
                mask //= 2
            if sum == S:
                return True, indices
        return False, None
