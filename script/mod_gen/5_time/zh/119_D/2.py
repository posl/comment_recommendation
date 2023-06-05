def get_min_distance(s,t,x):
    if x < s[0]:
        return s[0] - x
    elif x > t[-1]:
        return x - t[-1]
    else:
        min_distance = float("inf")
        for i in range(len(s)):
            if x >= s[i] and x <= t[i]:
                return 0
            else:
                if abs(s[i] - x) < min_distance:
                    min_distance = abs(s[i] - x)
                if abs(t[i] - x) < min_distance:
                    min_distance = abs(t[i] - x)
        return min_distance

if __name__ == '__main__':
    get_min_distance()