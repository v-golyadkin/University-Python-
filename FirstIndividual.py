char_array=input('Строка:')
counter=0
l=[]
for i in range(len(char_array)):
    if (char_array[i].isdigit()):
        counter=1
        tmp=int(char_array[i])
        l.append(tmp)
if (counter==1): print('Да')
else: print('Нет')
l.sort(reverse=True)
print(" ".join(map(str,l)))
