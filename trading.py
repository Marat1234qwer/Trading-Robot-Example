import strategy
import write_logs
import random
import matplotlib.pyplot as plt


def buy():
    global PROFIT
    PROFIT = PB.check(lst[i], PROFIT, i)


def sell():
    global PROFIT
    PROFIT = PS.check(lst[i], PROFIT, i)


def show_plot():
    x = []
    for i in range(len(lst)):
        x.append(i)
    plt.plot(x, lst, marker='o', color='b')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.show()


if __name__ == '__main__':
    PROFIT = 0
    lst = []
    curse = 110
    for _ in range(30):
        a = random.random()
        if a > 0.6:
            curse += 1
            lst.append(curse)
        elif a < 0.4:
            curse -= 1
            lst.append(curse)
        else:
            lst.append(curse)

    write_logs.write_lst_curse(lst)

    PB = strategy.PositionBuy()
    PB.count_pos = 1
    PB.buy_price = lst[0]

    PS = strategy.PositionSell()
    PS.count_pos = 1
    PS.sell_price = lst[0]

    for i in range(len(lst)):
        if PB.buy_price - lst[i] == 8 and PB.count_pos == 8:
            write_logs.fb_margine_call(time=(i+1), price=lst[i])
            print('MARGINE CALL from BUY Price: ', lst[i])
            print('----------------------------')
            break
        elif PS.sell_price - lst[i] == -8 and PS.count_pos == 8:
            write_logs.fs_margine_call(time=(i+1), price=lst[i])
            print('MARGINE CALL from SELL. Price: ', lst[i])
            print('------------------------------')
            break
        else:
            buy()
            sell()

    TOTAL_PROFIT = PROFIT + (lst[-1] * PB.count_pos - PB.buy_price * PB.count_pos) + \
        (PS.sell_price * PS.count_pos - lst[-1] * PS.count_pos)

    write_logs.write_report(lst[-1], PROFIT, PB.count_pos, PB.buy_price, PS.count_pos, PS.sell_price, TOTAL_PROFIT)

    print('Last price: ', lst[-1])
    print('TOTAL PROFIT: ', TOTAL_PROFIT)

    show_plot()
