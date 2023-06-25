import pandas as pd
from sklearn import linear_model
import tkinter as tk
from tkinter import messagebox

# Load the dataset
df = pd.read_csv("housepricesdataset.csv", sep=";")

# Create a linear regression model
reg = linear_model.LinearRegression()
reg.fit(df[['area', 'roomcount', 'buildingage']], df['price'])

# Create a Tkinter window
window = tk.Tk()
window.title("House Price Prediction")
window.configure(bg="#F0F0F0")

# Function to perform the prediction and display the result
def predict_price():
    try:
        area = float(entry_area.get())
        roomcount = float(entry_roomcount.get())
        buildingage = float(entry_buildingage.get())

        # Perform the prediction
        predicted_price = reg.predict([[area, roomcount, buildingage]])
        messagebox.showinfo("Prediction Result", f"The predicted price is: {predicted_price[0]}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create labels and entry fields for input
label_area = tk.Label(window, text="Area (in square meters):", bg="#F0F0F0", font=("Arial", 12))
label_area.pack()
entry_area = tk.Entry(window, font=("Arial", 12))
entry_area.pack()

label_roomcount = tk.Label(window, text="Number of rooms:", bg="#F0F0F0", font=("Arial", 12))
label_roomcount.pack()
entry_roomcount = tk.Entry(window, font=("Arial", 12))
entry_roomcount.pack()

label_buildingage = tk.Label(window, text="Building age (in years):", bg="#F0F0F0", font=("Arial", 12))
label_buildingage.pack()
entry_buildingage = tk.Entry(window, font=("Arial", 12))
entry_buildingage.pack()

# Create a button to trigger the prediction
button_predict = tk.Button(window, text="Predict", command=predict_price, font=("Arial", 12), bg="#4CAF50", fg="white")
button_predict.pack(pady=10)

# Create a label for the prediction result
result_label = tk.Label(window, text="", bg="#F0F0F0", font=("Arial", 12, "bold"))
result_label.pack()

# Function to update the prediction result label
def update_result_label(price):
    result_label.configure(text=f"The predicted price is: {price}")

# Start the Tkinter event loop
window.mainloop()
