from collections import Counter
st = input("Введите строку символов: \n")
c = Counter(st)
print(*c.most_common(3), sep='\n')

