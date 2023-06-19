def solution(s):
    days = ['monday','tuesday','wednesday','thursday','friday']
    if s == 'saturday':
        print(0)
    elif s == 'sunday':
        print(1)
    else:
        print(days.index('friday') - days.index(s) + 2)
