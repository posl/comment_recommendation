def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(M)]
    def f(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def g(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def h(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def i(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def j(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def k(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def l(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def m(s):
        if s in T:
            return False
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in T:
                    return False
        return True
    def n(s):
