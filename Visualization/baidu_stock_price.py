#coding: utf-8
# 将当前的日期减去1年作为起始日期
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import candlestick_ochl
import sys
from datetime import date

today = date.today()
start = (today.year - 1, today.month, today.day)

alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")

# 从财经频道下载股价数据
symbol = 'BIDU' # 百度的股票代码
quotes = quotes_historical_yahoo_ochl(symbol, start, today)

# 创建figure对象，这是绘图组件的顶层容器
fig = plt.figure()
# 增加一个子图
ax = fig.add_subplot(111)
# x轴上的主定位器设置为月定位器，该定位器负责x轴上较粗的刻度
ax.xaxis.set_major_locator(months)
# x轴上的次定位器设置为日定位器，该定位器负责x轴上较细的刻度
ax.xaxis.set_minor_locator(alldays)
# x轴上的主格式化器设置为月格式化器，该格式化器负责x轴上较粗刻度的标签
ax.xaxis.set_major_formatter(month_formatter)

# 使用matplotlib.finance包的candlestick函数绘制k线图
candlestick_ochl(ax, quotes)
# 将x轴上的标签格式化为日期
fig.autofmt_xdate()
plt.title('Baidu, Inc. (BIDU)')
plt.show()

