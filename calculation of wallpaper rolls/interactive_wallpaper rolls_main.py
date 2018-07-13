# coded by Nataliya Sashnikova
# Расчет рулонов обоев


def calc():
    global i
    i += 1
    h_area = float(input('высота участка: '))
    w_area = float(input('ширина участка: '))
    roll_num = math.ceil(math.ceil(w_area/w_roll)/math.floor(h_roll/h_area)) # количество рулонов
    spare_num = roll_num*math.floor(h_roll/h_area)-math.ceil(w_area/w_roll)  # в резерве - полос для данного участка

    print ("всего нужно полос: ", math.ceil(w_area/w_roll))
    print ("целых кусков (полос) для одного рулона: ", math.floor(h_roll/h_area))
    print ("количество рулонов: ", roll_num , "; количество полос: ", roll_num*math.floor(h_roll/h_area))
    print ("в резерве - полос: ", spare_num, " в резерве - метров: ", h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area)))
    print(roll_num, "рулон(а)(ов) для", i, "-го участка")

    sum_roll_num.append(roll_num)
    sum_spare.append(h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area)))

    answer = input('want another entry: (y/n) ?').lower()
    if answer == 'y':
        return calc()
    else:
        print('get result')
    return roll_num


if __name__ == '__main__':
    from wallpaper_rolls import *


sum_roll_num = []
sum_spare = []
i = 0
calc()

print("всего рулонов, шт.: ", reduce((lambda x, y: x + y), sum_roll_num))
print("всего резерв, м: ", reduce((lambda x, y: x + y), sum_spare))
