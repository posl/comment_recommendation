def is_majority(s):
    if s.count('For') > s.count('Against'):
        return True
    else:
        return False
n = int(input())
s = []
for i in range(n):
    s.append(input())

if __name__ == '__main__':
    is_majority()