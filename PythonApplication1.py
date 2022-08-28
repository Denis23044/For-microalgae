#Ввожу начальное время
print("Введите время посева")
try:
    h_begin=int(input("Часы: "))
    if h_begin<0 or h_begin>23 :
        raise ValueError

    m_begin=int(input("Минуты: "))
    if m_begin<0 or m_begin>59:
        raise ValueError
except:
    print('Необходимо ввести числа от 0 до 23 в графу "Часы" и число от 0 до 59 в графу "Минуты"')
    exit(0)
time_begin= h_begin*60 + m_begin #Время начала в минутах
#print(f"{time_begin}")

#Ввожу конечное время
print("Введите время, до которого биомасса будет расти")
try:
    h_end=int(input("Часы: "))
    if h_end<0 or h_end>23 :
        raise ValueError

    m_end=int(input("Минуты: "))
    if m_end<0 or m_end>59:
        raise ValueError
except:
    print('Необходимо ввести числа от 0 до 23 в графу "Часы" и число от 0 до 59 в графу "Минуты"')
    exit(0)
if h_begin>h_end :
    time_end= (h_end+24)*60 + m_end #Время конца в минутах
elif m_begin > m_end :
    time_end= (h_end+24)*60 + m_end #Время конца в минутах
else:
    time_end= h_end*60 + m_end #Время конца в минутах
#print(f"{time_end}")

time = time_end - time_begin #Время роста

#Ввожу время удвоения
print("Введите время удвоения")
try:
    h_double=int(input("Часы: "))
    if h_double<0 :
        raise ValueError

    m_double=int(input("Минуты: "))
    if m_double<0:
        raise ValueError
    double_time = h_double*60 + m_double
#    print(f"{double_time}")
    if double_time==0:
        raise ValueError
except:
    print('Необходимо ввести неотрицательные числа. Хотя бы одно из них не должно быть нулем')
    exit(0)

#Ввожу Остальные данные
try:
    in_density=float(input('Введите оптическую плотность инокулята:'))
    if in_density<=0:
        print("Оптическая плотность инокулята должна быть положительной")
        raise ZeroDivisionError

    end_density=float(input('Введите желаемую конечную оптическую плотность: '))
    if end_density<0:
        print("Конечная оптическая плотность не должна быть отрицательной")
        raise ZeroDivisionError

    volume=float(input('Введите объем колбы в мл: '))
    if volume<=0:
        print("Объем колбы должен быть положительным")
        raise ZeroDivisionError
except ValueError:
    print("Что-то пошло не так")
    exit(0)
except ZeroDivisionError:
    exit(0)

#Расчет
in_volume = (end_density*volume)/(in_density* (2**(time/double_time)) )
print(f"В колбу необходимо поместить {in_volume:.3f} мл инокулята")