def cooking_time(N, T):
    if N == 1:
        return T[0]
    elif N == 2:
        return max(T[0], T[1])
    else:
        T = sorted(T)
        t1 = T.pop()
        t2 = T.pop()
        t3 = T.pop()
        if t1 + t3 > t2 + t2:
            T.append(t1)
            T.append(t3)
            return t2 + cooking_time(N - 2, T)
        else:
            T.append(t1)
            T.append(t2)
            return t1 + cooking_time(N - 1, T)

if __name__ == '__main__':
    cooking_time()