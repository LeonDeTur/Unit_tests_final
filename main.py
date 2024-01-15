import random

import average_list

la = average_list.AverageList(random.sample(range(100), 10), random.sample(range(100), 10))
average0 = la.average_first_list
average1 = la.average_second_list

print(f"Первый список: {la.first_list}")
print(f"Второй список: {la.second_list}")
print()

if average0 > average1:
    print(f"Первый список имеет большее среднее значение ({average0}) чем второй список ({average1})")
elif average1 > average0:
    print(f"Второй список имеет большее среднее значение ({average1}) чем первый список ({average0})")
else:
    print(f"Средние значения первого и второго списка равны {average0}")