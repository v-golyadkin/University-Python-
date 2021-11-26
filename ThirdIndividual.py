def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
l=[]
with open('f.txt') as f:
    char_array = f.read().lower()

p=[]
j=[]
for i in range(len(char_array)):
    if (char_array[i].isdigit()):
        counter=1
        tmp=int(char_array[i])
        l.append(tmp)
if (counter==1): print('Да')
else: print('Нет')
l.sort(reverse=True)
print(l)
for i in range(1,len(l),2):
    p.append(l[i])
print(l)
for i in range(0,len(l),2):
    j.append(l[i])
print(l)
j.sort(reverse=False)
p.sort(reverse=True)
print(p)
print(j)
l.clear()
for i in range(len(p)):
        tmp=(p[i])
        l.append(tmp)
for i in range(len(j)):
        tmp=(j[i])
        l.append(tmp)
print(l)
if is_palindrome(l):print('Yes',l)
else:print('No')
