#Vytvor premenné meno a vek a vypíš vetu v tvare:
#"Ahoj, volám sa Meno a mám X rokov."

# meno = input("Ako sa volas?").capitalize()
# age = int(input("Kolko mas rokov?"))
# print(f"Ahoj,volam sa {meno} a mam {age} rokov")

#Maj dve premenné a a b. Pomocou f-stringu vypíš:
# "Súčet: X, Rozdiel: Y, Násobok: Z

# a = int(input("Zadaj cislo pre premennu a:"))
# b = int(input("Zadaj cislo pre premennu b:"))
# sucet = a + b
# print(f"{sucet}")
# rozdiel = a - b
# print(f"{rozdiel}")
# nasobok = a * b
# print(f"{nasobok}")

#Maj premennú cislo = 12.34567.
#Pomocou f-stringu vypíš číslo:
#na 2 desatinné miesta,
#na 4 desatinné miesta.

# x = 12.34567
# print(f"x is {x: .2f} ")
# x = 12.34567
# print(f"x is {x: .4f} ")

#Maj premenné:
#produkt = "Hrušky"
#cena = 1.5
#Vypíš to ako tabuľku v tvare:
# "Produkt | Cena"
# "Hrušky | 1.50 €"

# produkt = "Hrusky"
# cena = 1.5
# print(f"""
#       Produkt:{produkt}
#       Cena:{cena} £""")

#Vytvor tri premenné: meno, mesto, vek a vypíš ich pekne na riadky pomocou viacriadkového f-stringu.
# meno = input("Zadaj svoje meno:").capitalize()
# mesto = input("Zadaj svoje mesto:").capitalize()
# vek = int(input("Zadaj svoj vek:"))
# print(f"""
#       {meno}
#       {mesto}
#       {vek}""")

cisla = [12, 345, 7, 89, 1234]
#Úlohou je vytlačiť tabuľku:

#Číslo   | Dvojnásobok | Trojnásobok
#----------------------------------
#   12   | ...
#  345   | ...
#    7   | ...
#   89   | ...
# 1234   | ...
# Použi f-stringy so zarovnaním, aby boli všetky čísla pekne v stĺpcoch pod sebou.

# print(f"{"Cislo"} | {"Dvojnasobok":>10} | {"Trojnasobok":>10}")
# print("-" * 34 )
# for c in cisla:
#     print(f"{c:>4}  | {c * 2:>10}  | {c * 3:>10} ")