def runrun(n):
    if n > 10**9:
        return
    if n > 0:
        runrun_list.append(n)
    runrun(n*10 + n%10 - 1)
    runrun(n*10 + n%10)
    runrun(n*10 + n%10 + 1)
runrun_list = []
runrun(0)
K = int(input())
print(sorted(runrun_list)[K-1])

if __name__ == '__main__':
    runrun()