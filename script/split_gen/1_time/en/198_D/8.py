def alphametic(S1,S2,S3):
    if len(S1) != len(S2) or len(S2) != len(S3):
        return "UNSOLVABLE"
    N1 = [0]*len(S1)
    N2 = [0]*len(S2)
    N3 = [0]*len(S3)
    for i in range(len(S1)):
        if S1[i] == S2[i] and S2[i] == S3[i]:
            continue
        else:
            if S1[i] == S2[i]:
                N1[i] = 1
                N2[i] = 1
                if N3[i] == 0:
                    N3[i] = 2
            elif S2[i] == S3[i]:
                N2[i] = 1
                N3[i] = 1
                if N1[i] == 0:
                    N1[i] = 2
            elif S1[i] == S3[i]:
                N1[i] = 1
                N3[i] = 1
                if N2[i] == 0:
                    N2[i] = 2
            else:
                N1[i] = 1
                N2[i] = 1
                N3[i] = 2
    if N1[0] == 0 or N2[0] == 0 or N3[0] == 0:
        return "UNSOLVABLE"
    else:
        return N1,N2,N3
S1 = input()
S2 = input()
S3 = input()
print(alphametic(S1,S2,S3))
This is my code. It is not working for all the testcases. How do I fix it?
I am new to python and I am trying to find the sum of the list of numbers in python. I am using python 3.6. I am getting the following error:
Traceback (most recent call last):
  File "C:/Users/USER/AppData/Local/Programs/Python/Python36-32/Python36-32/Python36-32/python36-32.py", line 1, in <module>
    print(sum(list))
TypeError: 'int' object is not callable
This is the code:
list = [1, 2, 3
