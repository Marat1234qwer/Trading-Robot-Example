import write_logs


class PositionBuy:
    def __init__(self, count_pos=None, buy_price=None):
        self.count_pos = count_pos
        self.buy_price = buy_price

    def check(self, curse: int, profit: int, i: int):
        dif = curse - self.buy_price
        if dif < 0:
            self.average(dif, curse, i)
        elif dif == 1:
            profit = self.fix_profit(curse, profit, i)
        return profit

    def fix_profit(self, curse: int, profit: int, i):
        profit += self.count_pos
        self.buy_price = curse
        write_logs.fb_fix_profit(time=(i+1), curse=curse, count_pos=self.count_pos)
        self.count_pos = 1
        return profit

    def average(self, dif: int, curse: int, i):
        total = self.buy_price * self.count_pos
        if self.count_pos == 1 and dif == -2:
            self.buy_price = int((total + curse) / 2)
            self.count_pos += 1
            write_logs.fb_average(step=1, time=(i+1), curse=curse, count_pos=self.count_pos, buy_price=self.buy_price)

        elif self.count_pos == 2 and dif == -4:
            self.buy_price = int((total + (2 * curse)) / 4)
            self.count_pos += 2
            write_logs.fb_average(step=2, time=(i+1), curse=curse, count_pos=self.count_pos, buy_price=self.buy_price)
        elif self.count_pos == 4 and dif == -6:
            self.buy_price = int((total + (4 * curse)) / 8)
            self.count_pos += 4
            write_logs.fb_average(step=3, time=(i+1), curse=curse, count_pos=self.count_pos, buy_price=self.buy_price)


class PositionSell:
    def __init__(self, count_pos=None, sell_price=None):
        self.count_pos = count_pos
        self.sell_price = sell_price

    def check(self, curse: int, profit: int, i):
        dif = curse - self.sell_price
        if dif > 0:
            self.average(dif, curse, i)
        elif dif == -1:
            profit = self.fix_profit(curse, profit, i)
        return profit

    def fix_profit(self, curse: int, profit: int, i):
        profit += self.count_pos
        self.sell_price = curse
        write_logs.fs_fix_profit(time=(i+1), curse=curse, count_pos=self.count_pos)
        self.count_pos = 1
        return profit

    def average(self, dif: int, curse: int, i):
        total = self.sell_price * self.count_pos
        if self.count_pos == 1 and dif == 2:
            self.sell_price = int((total + curse) / 2)
            self.count_pos += 1
            write_logs.fs_average(step=1, time=(i+1), curse=curse, count_pos=self.count_pos, sell_price=self.sell_price)
        elif self.count_pos == 2 and dif == 4:
            self.sell_price = int((total + (2 * curse)) / 4)
            self.count_pos += 2
            write_logs.fs_average(step=2, time=(i+1), curse=curse, count_pos=self.count_pos, sell_price=self.sell_price)
        elif self.count_pos == 4 and dif == 6:
            self.sell_price = int((total + (4 * curse)) / 8)
            self.count_pos += 4
            write_logs.fs_average(step=3, time=(i+1), curse=curse, count_pos=self.count_pos, sell_price=self.sell_price)
