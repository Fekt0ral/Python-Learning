import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

msft = yf.Ticker('MSFT').history(period='6mo')

msft['Daily Return'] = msft['Close'].pct_change()
msft['Rolling Avg (7d)'] = msft['Close'].rolling(window=7).mean()
msft['Volatility (14d)'] = msft['Daily Return'].rolling(window=14).std()
#msft = msft.fillna(0)
msft['Growth Spike'] = msft['Daily Return'].apply(lambda x: True if abs(x) > 0.05 else False)

print(f"Mean: {msft['Daily Return'].mean()*100:.3f}%, median: {msft['Daily Return'].median()*100:.3f}%")
print(f"Largest drop: {msft['Daily Return'].idxmin().date()}, largest growth: {msft['Daily Return'].idxmax().date()}")
print(f"Spike days: {msft['Growth Spike'].sum()}")

msft.index = pd.to_datetime(msft.index)
most_volume_month = msft['Volume'].resample('ME').sum().idxmax()
print(f"Most volume month: {most_volume_month.strftime('%B')}")

plt.figure(figsize=(7.5, 3.5))
plt.plot(msft['Close'], label="Close Price")
plt.plot(msft['Rolling Avg (7d)'], label="7-Day SMA", linestyle="--")
plt.title("MSFT Stock Price & 7-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("msft_stock_price_&_7-day_moving_average.png")
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("+0+0")
except AttributeError:
    pass

plt.figure(figsize=(7.5, 3.5))
plt.bar(msft.index, msft['Daily Return']*100, label="Daily Return")
plt.title("MSFT Daily Return")
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("msft_daily_return.png")
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("+940+0")
except AttributeError:
    pass

plt.figure(figsize=(7.5, 3.5))
plt.plot(msft['Volatility (14d)'], label="Volatility (14d)")
plt.title("MSFT Volatility (14d)")
plt.xlabel("Date")
plt.ylabel("Volatility (Std of Daily Return)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("msft_volatility_14d.png")
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("-965+480")
except AttributeError:
    pass

spikes = msft.loc[msft['Growth Spike'], 'Daily Return']
spikes_dates = msft.index[msft['Growth Spike']]
plt.figure(figsize=(7.5, 3.5))
plt.bar(spikes_dates, spikes*100, label="Spikes Return")
plt.title("MSFT Spike Days Return")
plt.xlabel("Date")
plt.ylabel("Return (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("msft_spike_days_return.png")
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("+940+480")
except AttributeError:
    pass

plt.figure(figsize=(7.5, 3.5))
ax1 = plt.gca()
ax1.plot(msft['Volume'], label="Volume", color='tab:blue')
ax1.set_ylabel("Volume", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.plot(msft['Volatility (14d)'], label="Volatility (14d)", color='tab:orange', linestyle="--")
ax2.set_ylabel("Volatility (14d)", color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title("MSFT Volume & Volatility (14d)")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.savefig("msft_volume_&_volatility_14d.png")
manager = plt.get_current_fig_manager()
try:
    manager.window.wm_geometry("-510-340")
except AttributeError:
    pass

plt.show()

msft.to_csv("microsoft.csv", index=False)
#plt.show(block=False)
#plt.pause(5)
#plt.close('all')