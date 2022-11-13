from random import randint
def get_unique_list_numbers(lef,rin,n) -> list[int]:
      list_num =[]
      while len(list_num)<n and n<= len(range(lef,rin))+1:
              x = randint( lef, rin)
              if x not in list_num:
                list_num.append(x)
      return list_num

print(get_unique_list_numbers(-10, 10, 16))
