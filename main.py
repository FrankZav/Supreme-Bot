import time, sys, requests, hashlib, pygubu, json, os
from bs4 import BeautifulSoup
from splinter import Browser
from selenium import webdriver
import tkinter as tk

## GLOBAL VARIABLES
mainUrl = 'http://www.supremenewyork.com/shop/all/'
baseUrl = 'http://supremenewyork.com'
checkoutUrl = 'https://www.supremenewyork.com/checkout'

class Container:
    pass

class Bot:
    def __init__(self, gui):
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('bin\\gui.ui')
        self.mainwindow = builder.get_object('mainwindow', gui)
        self.console = builder.get_object('console')
        self.productlist = builder.get_object('listbox_products')
        builder.connect_callbacks(self)
        self.container = Container()
        self.builder.import_variables(self.container)
        self.load_payment_data()
    def load_payment_data(self):
        pass

def main():
	root = tk.Tk()
	root.wm_title("Supreme Drop Bot")
	root.wm_resizable(0,0)
	root.wm_iconbitmap("bin\\favicon.ico")
	root.mainloop()

if __name__ == '__main__':
    print("j",3)
    main()