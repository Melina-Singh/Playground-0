import tkinter as tk
import datetime      

nepali_digits = ["०", "१", "२", "३", "४", "५", "६", "७", "८", "९"]

nepali_months = ["बैशाख", "जेष्ठ", "असार", "श्रावण", "भाद्र", "आश्विन", "कार्तिक", "मंसिर", "पौष", "माघ", "फाल्गुन", "चैत"]

nepali_days_of_week = ["आइतवार", "सोमवार", "मंगलवार", "बुधवार", "बिहीवार", "शुक्रवार", "शनिवार"]

# The number of days in each Nepali month
days_in_nepali_month = [31, 31, 32, 31, 32, 30, 30, 30, 29, 30, 30, 31]
  
def get_nepali_digits(number):   
    """Converting a number to Nepali digits.""" 
    return ''.join(nepali_digits[int(digit)] for digit in str(number))

def get_nepali_month(month):
    return nepali_months[month - 1]

def get_nepali_day_of_week(day_of_week):
    return nepali_days_of_week[day_of_week]

def get_nepali_year(year):
    year_str = str(year)
    nepali_year = ''.join(nepali_digits[int(digit)] for digit in year_str)
    return nepali_year

def get_current_nepali_time():
    """Getting the current time in Nepali digits, month, and day of the week."""
    now = datetime.datetime.now()
    nepali_year = get_nepali_year(now.year + 56)
    nepali_month = (now.month + 8) % 12
    nepali_day = (now.day + 17)%30

    # Adjusting the day if it exceeds the number of days in the month
    while nepali_day > days_in_nepali_month[nepali_month]:
        nepali_month += 1
        if nepali_month >= len(days_in_nepali_month):
            nepali_month = 0
            nepali_year += 1
        nepali_day -= days_in_nepali_month[nepali_month]

    nepali_month = get_nepali_month(nepali_month + 1)
    nepali_day = get_nepali_digits(nepali_day)
    nepali_hour = get_nepali_digits(now.hour)
    nepali_minute = get_nepali_digits(now.minute)
    nepali_second = get_nepali_digits(now.second)
    
    # Here the day of the week is calculated using the Unix epoch as a reference
    days_since_epoch = (now - datetime.datetime(1970, 1, 1)).days
    day_of_week = (days_since_epoch + 4) % 7
    nepali_day_of_week = get_nepali_day_of_week(day_of_week)
    
    return nepali_year, nepali_month, nepali_day, nepali_hour, nepali_minute, nepali_second, nepali_day_of_week

def update_clock():
    """ the clock label with the current time."""
    nepali_year, nepali_month, nepali_day, nepali_hour, nepali_minute, nepali_second, nepali_day_of_week = get_current_nepali_time()
    clock_label.config(text=f"{nepali_day} {nepali_month} {nepali_year},{nepali_day_of_week}\n{nepali_hour}:{nepali_minute}:{nepali_second}")
    root.after(1000, update_clock)

# main window for the app
root = tk.Tk()
root.title("Nepali Digital Clock")
root.configure(bg='black')

# Create a label to display the clock
clock_label = tk.Label(root, font=("Helvetica", 36), bg='black', fg='#808A87')
clock_label.pack(padx=20, pady=20)

# Update the clock initially and start the clock update loop
update_clock()

# Start the Tkinter event loop
root.mainloop()
