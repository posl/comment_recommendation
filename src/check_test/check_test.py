import os

def check(path):
    test_l = sorted(os.listdir(path))
    if '.DS_Store' in test_l:
        test_l.remove('.DS_Store')
    for each_test in test_l:
        for difficulty in ['A', 'B', 'C', 'D']:
            in_l = sorted(os.listdir('{0}/{1}/{2}/in/'.format(path,each_test, difficulty)))
            out_l = sorted(os.listdir('{0}/{1}/{2}/out/'.format(path,each_test, difficulty)))
            if len(in_l) != len(out_l):
                print(each_test, difficulty, len(in_l), len(out_l))
                print(in_l)
                print(out_l)

def check_name(path):
    test_l = sorted(os.listdir(path))
    if '.DS_Store' in test_l:
        test_l.remove('.DS_Store')
    for each_test in test_l:
        for difficulty in ['A', 'B', 'C', 'D']:
            in_l = sorted(os.listdir('{0}/{1}/{2}/in/'.format(path,each_test, difficulty)))
            out_l = sorted(os.listdir('{0}/{1}/{2}/out/'.format(path,each_test, difficulty)))
            for i in range(len(in_l)):
                if in_l[i].split('.')[0] != out_l[i].split('.')[0]:
                    print(each_test, difficulty, in_l[i], out_l[i])

if __name__ == '__main__':
    check('/Users/keikoyanagi/Desktop/comment_recommendation/test_case')
    check_name('/Users/keikoyanagi/Desktop/comment_recommendation/test_case')