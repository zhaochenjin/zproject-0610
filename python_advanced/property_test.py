class Money(object):

    def __init__(self, dollars, cents):
        # self.dollars = dollars
        # self.cents = cents
        self.total_cents = dollars * 100 + cents

    @property   # getter 方法
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter  # setter 方法
    def dollars(self, dollars):
        self.total_cents = dollars * 100 + self.cents

    @property  # getter 方法
    def cents(self):
        return self.total_cents % 100

    @cents.setter  # setter 方法
    def cents(self, cents):
        # self.total_cents += cents
        self.total_cents = self.dollars * 100 + cents


money = Money(27, 12)
print('%d dollars %d cents.' % (money.dollars, money.cents))

money.dollars += 2  # mendy.dollars = money.dollars + 2
money.cents += 200
print('%d dollars %d cents.' % (money.dollars, money.cents))
