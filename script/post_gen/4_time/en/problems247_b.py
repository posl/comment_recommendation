Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n=int(input())
    st=[]
    for _ in range(n):
        s,t=input().split()
        st.append([s,t])
    return n,st

=======
Suggestion 2

def main():
    n = int(input())
    names = set()
    for i in range(n):
        s, t = input().split()
        names.add(s)
        names.add(t)
    if len(names) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

main()

=======
Suggestion 4

def get_input():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s_i, t_i = input().split()
        s.append(s_i)
        t.append(t_i)
    return n, s, t

=======
Suggestion 5

def main():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())

    for i in range(N):
        for j in range(i+1, N):
            if names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print("No")
                return
    print("Yes")

main()

=======
Suggestion 6

def main():
    n = int(input())
    names = []
    for _ in range(n):
        names.append(input().split())

    for i in range(n):
        for j in range(n):
            if i != j and names[i][0] == names[j][0] and names[i][1] == names[j][1]:
                print('No')
                return
    print('Yes')

=======
Suggestion 7

def main():
    n = int(input())
    nicknames = []
    for i in range(n):
        s, t = input().split()
        nicknames.append(s)
        nicknames.append(t)

    if len(nicknames) == len(set(nicknames)):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    n = int(input())
    ans = 'No'
    names = []
    for i in range(n):
        names.append(input().split(' '))
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    ans = 'Yes'
                    break
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    st = [input().split() for _ in range(n)]
    st_s = [s for s, t in st]
    st_t = [t for s, t in st]
    for i in range(n):
        if st_s[i] in st_t[:i]:
            print('Yes')
            return
        if st_t[i] in st_s[:i]:
            print('Yes')
            return
    print('No')

=======
Suggestion 10

def problem():
    #Get the number of people
    number_of_people = int(input())
    #Get the names of the people
    people_names = []
    for i in range(number_of_people):
        people_names.append(input().split())
    #Check if the names are valid
    for i in range(number_of_people):
        if people_names[i][0] in people_names[i][1:]:
            print("Yes")
            return
        elif people_names[i][1] in people_names[i][0:i] or people_names[i][1] in people_names[i][i+1:]:
            print("Yes")
            return
    print("No")
    return

problem()
