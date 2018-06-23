# app for calculating taxes
# functions + pandas
# coded by Nataliya Sashnikova


def compare(income):
    i = input('input money, local currency: ')
    j = income(float(i))
    print ('left, $:', j)
    got.append(i)
    left.append(int(j))
    answer = input('want another entry: (y/n) ?').lower()
    if answer == 'y':
        return compare(income)
    else:
        print('get result')


if __name__ == '__main__':
    from taxes import income, z
import pandas as pd
got = []
left = []
compare(income)
df = pd.DataFrame({'input number': [i for i in range(1, len(got) + 1)],
                   'local currency got': got,
                   'left, $': left,
                   'tax': [z for i in range(1, len(got) + 1)]
                  })
df.to_excel('C:\\Users\\user\PycharmProjects\\applications\\taxes application\\taxes.xlsx')
print(df)

'''
#-----------------------output-------------------------------------------------
input currency exchange rate: 8
input taxes: 18
input money, local currency: 700000
taxes, $: 15750.0
left, $: 71750.0
want another entry: (y/n) ?y
input money, local currency: 800000
taxes, $: 18000.0
left, $: 82000.0
want another entry: (y/n) ?y
input money, local currency: 900000
taxes, $: 20250.0
left, $: 92250.0
want another entry: (y/n) ?n
get result
   input number  left, $ local currency got   tax
0             1    71750             700000  18.0
1             2    82000             800000  18.0
2             3    92250             900000  18.0

'''
