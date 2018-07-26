# coded by Nataliya Sashnikova
# Расчет рулонов обоев


def calc():
    global i
    i += 1
    h_area = float(input('высота участка/ area height: '))
    w_area = float(input('ширина участка/ area width: '))
    pcs_num = math.floor(h_roll/h_area)                                             # целых кусков (полос) для одного рулона/ pieces q-ty for a roll
    roll_num = math.ceil(math.ceil(w_area/w_roll)/math.floor(h_roll/h_area))        # количество рулонов/ rolls q-ty
    spare_pcs_num = roll_num*math.floor(h_roll/h_area)-math.ceil(w_area/w_roll)     # в резерве полос для участка/ spare pieces for the area
    spare_metr = h_roll - h_area*(math.floor(h_roll/h_area ))                       # в резерве (метров) для одного рулона/ spare (metres/ inches) for one roll
    spare_metr_sum = h_roll*roll_num - h_area*roll_num*(math.floor(h_roll/h_area )) # в резерве (метров) для всех рулонов/ spare (metres/ inches) for roll for the area
    '''
    print ("всего нужно полос/ pieces req.: ", math.ceil(w_area/w_roll))
    print ("целых кусков (полос) для одного рулона/ pieces q-ty for a roll: ", pcs_num)
    print ("количество рулонов/ rolls q-ty: ", roll_num , " = количество полос/ pieces q-ty: ", roll_num*math.floor(h_roll/h_area))
    print ("в резерве полос/ spare pieces: ", spare_pcs_num, " в резерве метров/ spare metres: ", spare_metr_sum)
    print(roll_num, "рулон(а)(ов) для/ in sum rolls for", i, "-го участка/ -(st)(d)(th)area")
    '''
    sum_roll_num.append(roll_num)
    sum_spare.append(spare_metr_sum)
    d[i] = {"roll_num": roll_num, "h_area": h_area, "pcs_num": pcs_num, "spare_pcs_num": spare_pcs_num, "spare_metr": spare_metr, "spare_metr_sum": spare_metr_sum}
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

df = pd.DataFrame({'area number': [key for key in d],
                   'h_area': [d[key]['h_area'] for key in d],
                   'roll_num': [d[key]['roll_num'] for key in d],
                   'pcs_num': [d[key]['pcs_num'] for key in d],
                   'spare_pcs_num': [d[key]['spare_pcs_num'] for key in d],
                   'spare_metr': [d[key]['spare_metr'] for key in d],
                   'spare_metr_sum': [d[key]['spare_metr_sum'] for key in d]
                  })

# to find out if there is a spare in an area that can be used for another area. If it's so, it prints "yes"
def df_x():
    global x
    q = df.loc[x, 'h_area']
    df['spare can be used for ' + str(x + 1) + ' area'] = ["yes" if q <= df.loc[i, 'spare_metr'] and df.loc[x, 'roll_num'] <= df.loc[i, 'roll_num'] else 'N/A' for i in range(len(df.index))]
    return df['spare can be used for ' + str(x + 1) + ' area']


for x in range(len(df.index)):
    df_x()

print(df)
df.to_excel('C:\\Users\E277460\PycharmProjects\june 2018\\calculation of wallpaper rolls\\calc.xlsx')   # file contains rest of excel files
