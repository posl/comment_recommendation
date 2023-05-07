def main():
    K = int(input())
    
    def runrun(n):
        if n < 10:
            return True
        else:
            return (abs(int(str(n)[-1]) - int(str(n)[-2])) <= 1) and runrun(n // 10)
    
    def runrun_list(n):
        if n < 10:
            return [n]
        else:
            return [i for i in runrun_list(n // 10) if abs(int(str(n)[-1]) - int(str(i)[-1])) <= 1]
    
    def runrun_num(n):
        if n == 1:
            return 1
        else:
            return runrun_num(n - 1) + len(runrun_list(10 ** (n - 1)))
    
    def runrun_ans(n):
        if n < 10:
            return n
        else:
            return runrun_ans(n - 1) + len(runrun_list(10 ** (n - 1)))
    
    def runrun_k(k):
        if k <= 0:
            return 0
        elif k <= 9:
            return k
        else:
            for i in range(1, 10):
                if runrun_num(i) >= k:
                    return runrun_ans(i - 1) + runrun_list(10 ** (i - 1))[k - runrun_num(i - 1) - 1]
    
    print(runrun_k(K))
