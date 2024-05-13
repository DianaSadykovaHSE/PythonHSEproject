'''программа для посчета средней оценки работы бота'''
f=open('marks_bot')
k=0
n=0
for line in f:
    k+=1
    n+=int(line)
print(n/k)
