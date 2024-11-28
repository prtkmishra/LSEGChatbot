"""
process_data.py
Author: Prateek Mishra
Description:
    Methods to process the data and user inputs
"""
############################################################################################################################################

import json
import os
import pandas as pd

############################################################################################################################################

class Processor:
    """
    Class Processor to process and generate different ouputs 
    and save the information locally
    """
    def __init__(self) -> None:
        self.DATA_FILE = "./data/(TC3)Chatbot - stock data.json"
        self.data = self.load_data()
        self.df = pd.DataFrame(self.data)
        self.home_df = self.df[['code', 'stockExchange']]
        self.home_menu_filename = './temp/home_menu.csv'
        # Check if the stock_menu.csv file has been created by show_stock_menu()
        self.stock_menu_filename = './temp/stock_menu.csv'
        if os.path.exists(self.stock_menu_filename):
            self.stockmenu_df = pd.read_csv(self.stock_menu_filename)

    def load_data(self):
        """
        Load stock data from JSON file.
        """
        if not os.path.exists(self.DATA_FILE):
            return {"error": "Data file not found."}
        with open(self.DATA_FILE, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return {"error": "Invalid JSON file."}

    def home_menu(self):
        """
        Return the home menu and save it as a csv
        """
        try:
            # Save the home_menu.csv for future reference
            self.home_df.to_csv(self.home_menu_filename, index = False)
            return self.home_df
        except Exception as e:
            return f'Error: {e}'

    
    def stock_exchange(self):
        """
        Return the stock exchange list
        """
        try:
            return self.home_df['stockExchange'].to_list()
        except Exception as e:
            return f'Error: {e}'
    
    def show_stock_menu(self, stock_exchange:str):
        """
        Return the stock menu
        args: stock_exchange: str: name of the stock exchange
        return: stock menu
        """
        try:
            stock_exchange = stock_exchange.strip()
            stockmenu = self.df[self.df['stockExchange'] == stock_exchange ]['topStocks'].to_list()
            self.stockmenu_df = pd.DataFrame(stockmenu[0])
            self.stockmenu_df.to_csv(self.stock_menu_filename, index = False) # Save the sotck_menu.csv for future reference
            return self.stockmenu_df
        except Exception as e:
            return f'Error: {e}'
    
    def stock_values(self, stockname:str)-> str:
        """
        args: stockname: str: name of the stock for which price needs to  be checked
        return: price of the stock: str
        """
        try:
            stockname = stockname.strip()
            stock_value = self.stockmenu_df[self.stockmenu_df['stockName'] == stockname]['price'].to_string(index=False)
            return str(f'Stock Price of {stockname} is {stock_value}.\n Please select an option from below\n1. home\n2. go back')
        except Exception as e:
            return f'Error: {e}'
    
if __name__ == '__main__':
    objprocess = Processor()