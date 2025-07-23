import pandas as pd

class InventoryAgent:
    def __init__(self, data):
        self.data = data

    def check_reorder(self):
        return self.data[self.data["Stock"] < self.data["Reorder_Level"]]

class SalesAgent:
    def __init__(self, data):
        self.data = data

    def analyze_sales(self):
        return self.data.sort_values(by="Sales_Last_Month", ascending=False)

class LogisticsAgent:
    def __init__(self, data):
        self.data = data

    def calculate_delivery_priority(self):
        return self.data.sort_values(by="Lead_Time_Days")
