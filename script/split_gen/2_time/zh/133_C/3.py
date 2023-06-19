def main():
    L, R = map(int, input().split())
    min = 2018
    for i in range(L, R):
        for j in range(i+1, R+1):
            if min > i*j%2019:
                min = i*j%2019
                if min == 0:
                    print(min)
                    return
    print(min)
