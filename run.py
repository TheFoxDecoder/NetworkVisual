from networkCalculated import BLOCK4,NetworkData,NeuronConnectionCalcuator
import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Data Calculator")

        self.label_nodes = ttk.Label(root, text="Enter the total number of nodes:")
        self.label_conn_ratio = ttk.Label(root, text="Enter the connection ratio (1 : conn_ratio):")

        self.entry_nodes = ttk.Entry(root)
        self.entry_conn_ratio = ttk.Entry(root)

        self.button_calculate = ttk.Button(root, text="Calculate", command=self.calculate_network_data)
        
        self.result_text = tk.Text(root, height=10, width=40, state="disabled")

        # Layout
        self.label_nodes.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_nodes.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.label_conn_ratio.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_conn_ratio.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        self.button_calculate.grid(row=2, column=0, columnspan=2, pady=10)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    def calculate_network_data(self):
        try:
            nodes = int(self.entry_nodes.get())
            conn_ratio = int(self.entry_conn_ratio.get())
            calculator = NeuronConnectionCalcuator(nodes=nodes, conn_ratio=conn_ratio)
            result = calculator.calculate_network_data()

            # Display the calculated network data
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Calculated Network Data:\n{result}")
            self.result_text.config(state="disabled")

        except ValueError:
            self.result_text.config(state="normal")
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", "Invalid input. Please enter valid numeric values.")
            self.result_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

