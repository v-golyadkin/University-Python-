condidates=int(input("Кол-во кандидатов"))
dict={}
for i in range(condidates):
    condidate=(input("Кандидат "))
    count=int(input("Кол-во отданых голосов "))
    dict[condidate]=count
sorted_dict = sorted(dict.items(), key=lambda x: x[0])
print(sorted_dict)
