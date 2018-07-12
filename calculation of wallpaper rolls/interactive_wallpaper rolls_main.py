# coded by Nataliya Sashnikova
# Расчет рулонов обоев


def s():
    global i
    i += 1
    a = float(input('высота участка: '))
    b = float(input('ширина участка: '))
    print ("всего нужно полос: ", math.ceil(b/y))
    print ("целых кусков (полос) для одного рулона: ", math.floor(x/a))
    z = math.ceil(math.ceil(b/y)/math.floor(x/a))
    print ("количество рулонов: ", z , "; количество полос: ", z*math.floor(x/a))
    p = z*math.floor(x/a)-math.ceil(b/y)
    print ("в резерве полос: ", p)
    q.append(z)
    spare.append(x - (z*math.floor(x/a)*a))
    print(z, "рулонов для", i, "-го участка")
    answer = input('want another entry: (y/n) ?').lower()
    if answer == 'y':
        return s()
    else:
        print('get result')
    return z


if __name__ == '__main__':
    from wallpaper_rolls import *


q = []
spare = []
i = 0
s()

print("всего рулонов, шт.: ", reduce((lambda x, y: x + y), q))
print("всего резерв, м: ", reduce((lambda x, y: x + y), spare))
