import pandas as pd

def get_product_info(product_id):
    bank_products = pd.read_csv("data/bank_products.csv")
    product = bank_products[bank_products["product_id"] == product_id].iloc[0]
    return product

def calculate_return(investment_amount, interest_rate, deposit_period):
    return (investment_amount * interest_rate * deposit_period) / 36500  # Формула для расчёта доходности по депозиту
