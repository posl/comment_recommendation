def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
            return
        else:
            print(0)
            return
    else:
        d = int(max(list(X)))
        def base_n_to_10(X, n):
            out = 0
            for i in range(1,len(str(X))+1):
                out += int(X[-i])*(n**(i-1))
            return out
        
        def base_10_to_n(X, n):
            out = ''
            if (int(X/n)):
                out += base_10_to_n(int(X/n), n)
            out += str(X%n)
            return out
        
        def check(n):
            if n <= M:
                return True
            else:
                return False
        
        def binary_search(ok, ng):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if check(base_n_to_10(X, mid)):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        print(binary_search(0, M+1) - d)
