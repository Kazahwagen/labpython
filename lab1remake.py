#Номер 1 лабораторная 1
N = int(input('Введите оклад сотрудника:'))

nameone,nametwo,namethree = input('Введите имя первого сотрудника'),input('Введите имя второго сотрудника'),input('Введите имя третьего сотрудника')

N1,N2,N3 = int(input('Введите оклад первого сотрудника')),int(input('Введите оклад второго сотрудника')),int(input('Введите оклад третьего сотрудника'))

KvartPrem = 3000
rem = N * 2/3

podnalog = N - 0.13 * N

print(f'Квартальная премия:{KvartPrem}')

print(f'Сумма после уплаты подоходного налога: {podnalog}')
KvartPrem = N1 * 2/3
podnalog = N1 - 0.13*N1
print(f'Премия первого сотрудника: {KvartPrem}, Общий итог: {podnalog} ')

KvartPrem = N2 * 2/3
podnalog = N2 - 0.13*N2
print(f'Премия второго сотрудника: {KvartPrem}, Общий итог: {podnalog} ')

KvartPrem = N3 * 2/3
podnalog = N3 - 0.13*N3
print(f'Премия третьего сотрудника: {KvartPrem}, Общий итог: {podnalog} ')