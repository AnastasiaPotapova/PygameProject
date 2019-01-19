n = int(input())
a = int(input())
b = int(input())
s = input()
a_ans = []
b_ans = []
if b + a*2 > s.count('0'):
    print('NO')
else:
    for i in range(n-1):
        if s[i] == '0' and s[i+1] == '0' and not(i in a_ans or i+1 in a_ans) and a>0:
            a -= 1
            a_ans.append(i)
            a_ans.append(i+1)
        elif s[i] == '0' and s[i+1] != '0' and not(i in a_ans) and b>0:
            b -= 1
            b_ans.append(i+1)

    if b>0:
        while b>0 and i<n:
            if s[i] ==  '0' and not(i in a_ans or i in b_ans):
                b_ans.append(i)
                b -= 1
                i += 1
    b_ans.sort()

    if a == 0 and b == 0:
        print('YES')
        for i in range(0, len(a_ans), 2):
            print(a_ans[i]+1, a_ans[i+1]+1)
        for i in b_ans:
            print(i)
    else:
        print('NO')
