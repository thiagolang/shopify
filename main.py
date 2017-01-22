# shopify career intro #
# Author/Date: Thiago Lang - Jan-22 #
# Program: Read Order Overview #

import json
from urllib.request import urlopen


# read json input #
def read_input(order_url):
    url_response = urlopen(order_url)
    parsed_order_file = json.loads(url_response.read().decode())
    return parsed_order_file


# calculate the total revenue from the orders page N #
def calculate_total_revenue(orders_input, page):
    order_page_revenue = 0.0
    orders = read_input(orders_input + str(page))

    for order in orders['orders']:
        order_page_revenue += float(order['total_price'])

    return round(order_page_revenue,2)


# --- MAIN PROGRAM --- #
def main():
    # initiate params #
    orders_url = "https://shopicruit.myshopify.com/admin/orders.json?access_token=c32313df0d0ef512ca64d5b336a0d7c6&page="
    orders_exist = True
    orders_page = 1
    total_revenue = 0.0

    # while revenue per page is more than 0 than keep adding to total_revenue #
    while orders_exist:
        order_revenue = calculate_total_revenue(orders_url, orders_page)
        if order_revenue > 0:
            total_revenue += order_revenue
        else:
            orders_exist = False
        orders_page += 1
    return total_revenue

print(main())