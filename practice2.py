# Zadanie: Vizitka s f-string
#
# Napíš program, ktorý od používateľa získa tieto údaje:
#
# meno
#
# priezvisko
#
# vek
#
# mesto
#
# Pomocou f-stringov vypíš na obrazovku vizitku v tomto formáte:

# vizitka = {
#     "meno": "Vojtech",
#     "priezvisko": "Timura",
#     "vek": 45,
#     "mesto": "Bristol"
# }
# print(vizitka)
#
# print(f"""
#
# Vizitka: {vizitka["meno"]} {vizitka["priezvisko"]}
# Vek: {vizitka["vek"]} rokov
# Mesto: {vizitka["mesto"]}
# """)
# print(vizitka)

# meno = input("Zadaj meno: ")
# priezvisko = input("Zadaj priezvisko: ")
# vek = int(input("Zadaj vek: "))
# mesto = input("Zadaj mesto: ")
#
# vizitka = {
#     "meno": meno,
#     "priezvisko": priezvisko,
#     "vek": vek,
#     "mesto": mesto,
# }
#
# print(f"""
# Vizitka
# Meno: {vizitka["meno"].capitalize()} {vizitka["priezvisko"].capitalize()}
# Vek: {vizitka["vek"]} rokov
# Mesto: {vizitka["mesto"].capitalize()}
# """)

#Cestovny listok
#
# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# end_of_destination = input("Enter your end of destination: ")
# long_in_hours = int(input("Enter your long in hours: "))
# price_of_ticket = int(input("Enter your price per ticket: "))
# price_for_two = (price_of_ticket * 2)
# ticket = {
#     "Name": name,
#     "Surname": surname,
#     "End_of_destination": end_of_destination,
#     "Long_in_hours": long_in_hours,
#     "Price_of_ticket": price_of_ticket,
#     "Price_for_two": price_for_two
# }
#
# print(ticket)
#
# # print(f"""
# # Ticket
# # name: {ticket["Name"].capitalize()} {ticket["Surname"].capitalize()}
# # end_of_destination: {ticket["End_of_destination"].capitalize()}
# # long_in_hours: {ticket["Long_in_hours"]}
# # price_of_ticket: {ticket["Price_of_ticket"]} pounds
# # """)
#
# print(f"Traveler {ticket["Name"].capitalize()} {ticket["Surname"].capitalize()} is traveling to {ticket["End_of_destination"].capitalize()}.Journey will take "
#       f"{ticket["Long_in_hours"]} an hours and price is {ticket["Price_of_ticket"]} pounds. If do you want one more ticket,so {ticket["Price_for_two"] } pounds.")

first_customer_name = input("Enter your name: ").capitalize()
first_customer_surname = input("Enter your surname: ").capitalize()
second_customer_name = input("Enter your name: ").capitalize()
second_customer_surname = input("Enter your surname: ").capitalize()
name_of_food = input("Enter name of your food: ").capitalize()
price_of_food = int(input("Enter price of your food: "))
drink_name = input("Enter drink name: ").capitalize()
price_of_drink = int(input("Enter price of your drink: "))
name_of_food_2 = input("Enter name of your food: ").capitalize()
price_of_food_2 = int(input("Enter price of your food: "))
drink_name_2 = input("Enter drink name: ").capitalize()
price_of_drink_2 = int(input("Enter price of your drink: "))

result = price_of_food + price_of_drink
result1 = price_of_food_2 + price_of_drink_2
result2 = result + result1

print(f"""
      first_customer_name : {first_customer_name} {first_customer_surname}
      second_customer_name : {second_customer_name} {second_customer_surname}
      name_of_food : {name_of_food} and {name_of_food_2}
      price_of_food : ({price_of_food})£ and ({price_of_food_2}) £
      drink_name : {drink_name} and {drink_name_2}
      price_of_drink : ({price_of_drink})£ and ({price_of_drink_2})£
      result : {result2} £
      """)


# order = {
#     "customer_name": customer_name,
#     "name_of_food": name_of_food,
#     "price_of_food": price_of_food,
#     "drink_name": drink_name,
#     "price_of_drink": price_of_drink,
#     "result": result
#
# }
# print(order)

# print(f"""
# Customer name: {customer_name},
# Customer surname: {customer_surname},
# Name of food: {name_of_food},
# Price of food: {price_of_food},
# Drink: {drink_name},
# Price of drink: {price_of_drink},
# Result: {result}
# """)

# print(f"""
# ----------------------
# Restaurant Order
# Customer: {customer_name} {customer_surname}
# Food: {name_of_food} ({price_of_food} €)
# Drink: {drink_name} ({price_of_drink} €)
# Total price: {result} €
# ----------------------
# """)



