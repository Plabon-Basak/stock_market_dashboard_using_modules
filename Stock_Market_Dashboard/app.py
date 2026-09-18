import os
import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load Stock Data
def load_data(file_path=os.path.join(BASE_DIR, "stock_data.csv")):
	return pd.read_csv(file_path)

data = load_data()
stocks = sorted(data["stock"].unique())

# Initialize Tkinter App
root = tk.Tk()
root.title("Stock Market Dashboard")
root.geometry("700x600")

# Control frame (fixed at top) and display frame (chart area below)
control_frame = tk.Frame(root)
control_frame.pack(side="top", fill="x", pady=5)

display_frame = tk.Frame(root)
display_frame.pack(side="top", fill="both", expand=True)

# Global variables for current chart / stats widget
current_canvas = None
current_stats = None

def clear_display():
    global current_canvas, current_stats
    for widget in display_frame.winfo_children():
        widget.destroy()
    current_canvas = None
    current_stats = None

def plot_stock_data(stock):
    clear_display()
    if not stock:
        return

    filtered_data = data[data["stock"] == stock].copy()
    filtered_data["date"] = pd.to_datetime(filtered_data["date"])
    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot(filtered_data["date"], filtered_data["price"], marker="o")
    ax.set_title(f"{stock} Stock Prices")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    fig.autofmt_xdate()

    current_canvas = FigureCanvasTkAgg(fig, master=display_frame)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(fill="both", expand=True)

def compare_stocks(stock1, stock2):
    clear_display()
    if not stock1 or not stock2:
        return

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    for stock in (stock1, stock2):
        filtered_data = data[data["stock"] == stock].copy()
        filtered_data["date"] = pd.to_datetime(filtered_data["date"])
        ax.plot(filtered_data["date"], filtered_data["price"], marker="o", label=stock)
    ax.set_title(f"Comparison: {stock1} vs {stock2}")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend()
    ax.grid(True)
    fig.autofmt_xdate()

    current_canvas = FigureCanvasTkAgg(fig, master=display_frame)
    current_canvas.draw()
    current_canvas.get_tk_widget().pack(fill="both", expand=True)

def show_statistics(stock):
    clear_display()
    if not stock:
        return

    prices = data[data["stock"] == stock]["price"]
    lines = [
        f"{stock}:",
        f"  Average: {prices.mean():.2f}",
        f"  Min: {prices.min():.2f}  Max: {prices.max():.2f}",
        f"  Std Dev: {prices.std():.2f}",
        f"  Data Points: {len(prices)}",
    ]

    global current_stats
    current_stats = tk.Text(display_frame, height=8, width=40, font=("Arial", "12"))
    current_stats.insert("1.0", "\n".join(lines))
    current_stats.config(state="disabled")
    current_stats.pack(pady=5)

# --- Widgets ---

# Dropdown for selecting stock
stock_label = tk.Label(control_frame, text="Select Stock:")
stock_label.pack(pady=5)
stock_dropdown = ttk.Combobox(control_frame, values=stocks)
stock_dropdown.pack(pady=5)

# Button to plot data
plot_button = tk.Button(control_frame, text="Plot Stock Data", command=lambda: plot_stock_data(stock_dropdown.get()), font=("Arial", "12"))
plot_button.pack(pady=5)

# Button to show statistics
stats_button = tk.Button(control_frame, text="Show Statistics", command=lambda: show_statistics(stock_dropdown.get()), font=("Arial", "12"))
stats_button.pack(pady=5)

# Button to compare stocks (reveals the comparison options)
def toggle_compare():
    if compare_frame.winfo_manager():
        compare_frame.pack_forget()
    else:
        compare_frame.pack(pady=5)
        clear_display()

compare_button = tk.Button(control_frame, text="Compare Stocks", command=toggle_compare, font=("Arial", "12"))
compare_button.pack(pady=5)

# Comparison frame (hidden until Compare Stocks is clicked)
compare_frame = tk.Frame(control_frame)

compare1_label = tk.Label(compare_frame, text="Select Stock 1:")
compare1_label.pack(pady=5)
compare1_dropdown = ttk.Combobox(compare_frame, values=stocks)
compare1_dropdown.pack(pady=5)

compare2_label = tk.Label(compare_frame, text="Select Stock 2:")
compare2_label.pack(pady=5)
compare2_dropdown = ttk.Combobox(compare_frame, values=stocks)
compare2_dropdown.pack(pady=5)

compare_plot_button = tk.Button(compare_frame, text="Plot Comparison", command=lambda: compare_stocks(compare1_dropdown.get(), compare2_dropdown.get()), font=("Arial", "12"))
compare_plot_button.pack(pady=5)

root.mainloop()