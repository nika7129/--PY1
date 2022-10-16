src = not False and True or False and not True #исходное выражение

# result = and True or False and # избавляемся от отрицаний
# result = True or False # избавляемся от "И"
# result = True # избавляемся от "ИЛИ"

result= True
print(src == result)
