from tkinter import *

#creating the function of calculating the miles to km
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

# creating the window or screen
window = Tk()
window.minsize(width=100, height=150)
# providing the window name
window.title("Miles to kilometer Converter")

# giving the window spacing
window.config(padx=20, pady=20)
# Creating Wadgets
# Entry for miles
miles_input = Entry(width=7)
# using the grid function to place the wadget on the screen
miles_input.grid(column=1, row=0)

# label
mile_label = Label(text="Miles")
# using the grid function to place the wadget on the screen
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
# using the grid function to place the wadget on the screen
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
# using the grid function to place the wadget on the screen
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="km")
# using the grid function to place the wadget on the screen
kilometer_label.grid(column=2, row=1)

# button
calculate_button = Button(text="Calculater", command=miles_to_km)
# using the grid function to place the wadget on the screen
calculate_button.grid(column=1, row=2)


# keep the window ON
window.mainloop()



