def main():
    # get input
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    #print(s)
    # find the most votes
    max_vote = 0
    max_name = ""
    for name in s:
        if s.count(name) > max_vote:
            max_vote = s.count(name)
            max_name = name
    #print(max_vote)
    #print(max_name)
    # print the name
    print(max_name)
