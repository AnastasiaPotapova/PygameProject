shagi = input()
chislo = []
for _ in range(len(shagi)):
    chislo.append(0)
n = 0
k = 1
while n<len(shagi):
    if shagi[n] == '+':
        chislo[k] = chislo[k] + 1
    elif shagi[n] == '-':
        chislo[k] = chislo[k] -1
    elif shagi[n] == '<':
        k = k-1
    elif shagi[n] == '>':
        k = k+1
    elif shagi[n] == '.':
        if chislo[k]<0:
            chislo[k] = 256 + chislo[k]
        print(chislo[k])
    n = n+1
    