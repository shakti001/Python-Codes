t1 = 'monday','wednesday','thursday','saturday'
t1 = t1[:1] + ('tuesday',) + t1[1:]
t1 = t1[:4] + ('friday',) + t1[4:]
print(t1)
