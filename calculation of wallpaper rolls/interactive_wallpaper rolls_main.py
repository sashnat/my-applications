# coded by Nataliya Sashnikova
# Расчет рулонов обоев


def calc():
    global i
    i += 1
    h_area = float(input('высота участка/ area height: '))
    w_area = float(input('ширина участка/ area width: '))
    roll_num = math.ceil(math.ceil(w_area/w_roll)/math.floor(h_roll/h_area)) # количество рулонов
    spare_num = roll_num*math.floor(h_roll/h_area)-math.ceil(w_area/w_roll)  # в резерве - полос для данного участка
    spare_metr = h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area ))

    print ("всего нужно полос/ pieces req.: ", math.ceil(w_area/w_roll))
    print ("целых кусков (полос) для одного рулона/ pieces q-ty for a roll: ", math.floor(h_roll/h_area))
    print ("количество рулонов/ rolls q-ty: ", roll_num , "; количество полос/ pieces q-ty: ", roll_num*math.floor(h_roll/h_area))
    print ("в резерве полос/ spare pieces: ", spare_num, " в резерве метров/ spare metres: ", spare_metr)
    print(roll_num, "рулон(а)(ов) для/ in sum rolls for", i, "-го участка/ -(st)(d)(th)area")

    sum_roll_num.append(roll_num)
    sum_spare.append(h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area)))
    d[i] = {"h_area": h_area, "spare_num": spare_num, "spare_metr": spare_metr}

    answer = input('want another entry: (y/n) ?').lower()
    if answer == 'y':
        return calc()
    else:
        print('get result')
    return roll_num


if __name__ == '__main__':
    from wallpaper_rolls import *

d = {}
sum_roll_num = []
sum_spare = []
i = 0
calc()


print("всего рулонов, шт./ rolls in sum req :", reduce((lambda x, y: x + y), sum_roll_num))
print("всего резерв, м / spare in sum:", reduce((lambda x, y: x + y), sum_spare))
#print(d)
df = pd.DataFrame({'h_area': [d[key]['h_area'] for key in d],
                   'spare_num': [d[key]['spare_num'] for key in d],
                   'spare_metr': [d[key]['spare_metr'] for key in d]
                  })
df.to_excel('C:\\Users\E277460\PycharmProjects\june 2018\\calculation of wallpaper rolls\\calc.xlsx')   # file contains rest of excel files
print(df)
