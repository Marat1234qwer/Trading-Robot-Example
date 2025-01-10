def write_lst_curse(lst):
    with open('logs.txt', 'a') as f:
        f.writelines(str(lst) + '\n')

def fb_margine_call(time, price):
    with open('logs.txt', 'a') as f:
        f.writelines(f'Time {time} :FROM BUY: MARGINE CALL. Price: {price}\n')

def fs_margine_call(time, price):
    with open('logs.txt', 'a') as f:
        f.writelines(f'Time {time} :FROM SELL: MARGINE CALL. Price: {price}\n')

def fb_fix_profit(time, curse, count_pos):
    with open('logs.txt', 'a') as f:
        f.writelines(f'Time {time} :FROM BUY: Curse={curse}. Fix profit +{count_pos}\n')

def fs_fix_profit(time, curse, count_pos):
    with open('logs.txt', 'a') as f:
        f.writelines(f'Time {time} :FROM SELL: Curse={curse}. Fix profit +{count_pos}\n')

def fb_average(step, time, curse, count_pos, buy_price):
    if step == 1:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM BUY: Curse={curse}, Average. Buy 1 lot. Balance {count_pos} for {buy_price}\n')
    elif step == 2:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM BUY: Curse={curse}, Average. Buy 2 lots. Balance {count_pos} for {buy_price}\n')
    elif step == 3:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM BUY: Curse={curse}, Average. Buy 4 lots. Balance {count_pos} for {buy_price}\n')

def fs_average(step, time, curse, count_pos, sell_price):
    if step == 1:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM SELL: Curse={curse}, Average. Sell 1 lot. Balance {count_pos} for {sell_price}\n')
    elif step == 2:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM SELL: Curse={curse}, Average. Sell 2 lots. Balance {count_pos} for {sell_price}\n')
    elif step == 3:
        with open('logs.txt', 'a') as f:
            f.writelines(f'Time {time} :FROM SELL: Curse={curse}, Average. Sell 4 lots. Balance {count_pos} for {sell_price}\n')
    
def write_report(last_price, profit, b_count, b_price, s_count, s_price, total):
    strings = []
    string1 = f'Last price: {last_price}. Profit = {profit}\n'
    string2 = f'Balance: BUY = {b_count} for {b_price}, SELL = {s_count} for {s_price}\n'
    string3 = f'After closing position TOTAL PROFIT = {total}\n'
    strings.append(string1)
    strings.append(string2)
    strings.append(string3)
    strings.append('---------------------------------------------------------------' + '\n\n')
    with open('logs.txt', 'a') as f:
        f.writelines(strings)