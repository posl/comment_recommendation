def check_honesty(honesty, people, testimonies):
    for i in range(people):
        if honesty[i] == 1:
            for testimony in testimonies[i]:
                if honesty[testimony[0]-1] != testimony[1]:
                    return False
    return True
