import yfinance as yf
import matplotlib.pyplot as plt

nvda = yf.Ticker("NVDA").history(period="3mo")

plt.plot(nvda["Close"])

nvda["Close_rolling_7"] = nvda["Close"].rolling(window=7).mean()
plt.plot(nvda["Close_rolling_7"])
plt.show()

print(f"Максимальная цена закрытия: {nvda['Close'].max():.2f}, минимальная цена закрытия: {nvda['Close'].min():.2f}")
print(f"Средний дневной объем торгов: {nvda['Volume'].mean():.2f}")

print()

dates = []
for i in range (1, len(nvda["Close"])):
    if nvda["Close"].iloc[i] > nvda["Close"].iloc[i - 1] * 1.05:
        dates.append(nvda.index[i].date())

print()

if dates:
    print("Даты, когда цена выросла более чем на 5%:")
    for d in dates:
        print(d)
else:
    print("Нет дней с ростом цены более чем на 5%.")