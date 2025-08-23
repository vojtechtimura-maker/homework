# #Homework 1.(lesson 3)
#
# books = [
#     {
#         "name": "Pán prstenů: Společenstvo prstenu",
#         "price": 500,
#         "author": "J.R.R. Tolkien",
#         "publication_year": 1954,
#     }
# ]
#
# # 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.
#
# books.append({
#     "name": "Pokemon",
#     "price": 200,
#     "author": "Pikachu",
#     "publication_year": 1044,
# })
# books.append({
#     "name": "Hulk",
#     "price": 100,
#     "author": "Hogan",
#     "publication_year": 1876,
# })
#
# print(f"{books[0]["name"]} , {books[0]["price"]} , {books[0]["author"]} , {books[0]["publication_year"]}")
# print(f"{books[1]["name"]} , {books[1]["price"]} , {books[1]["author"]} , {books[1]["publication_year"]}")
# print(f"{books[2]["name"]} , {books[2]["price"]} , {books[2]["author"]} , {books[2]["publication_year"]}")
#
#
# # 2. Změň cenu jedné libovolné knihy. Vypiš list.
#
# books[0]["price"] = int(str(books[0]["price"]).replace("500" , "400"))
# print(f"{books[0]["name"]} , {books[0]["price"]} , {books[0]["author"]} , {books[0]["publication_year"]}")
# print(f"{books[1]["name"]} , {books[1]["price"]} , {books[1]["author"]} , {books[1]["publication_year"]}")
# print(f"{books[2]["name"]} , {books[2]["price"]} , {books[2]["author"]} , {books[2]["publication_year"]}")
#
#
# # 3. Odstraň nějakou knihu. Vypiš list.
#
# del books[1]
# print(f"{books[0]["name"]} , {books[0]["price"]} , {books[0]["author"]} , {books[0]["publication_year"]}")
# print(f"{books[1]["name"]} , {books[1]["price"]} , {books[1]["author"]} , {books[1]["publication_year"]}")
#
# # 4. Vypiš celkový počet knih v listu.
#
# print(len(books))
#
# # Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)
#
# nazov3 = input("Zadaj nazov knihy:")
# cena3 = int(input("Zadaj cenu knihy:"))
# author3 = input("Zadaj meno autora:")
# publication_year3 = int(input("Zadaj publication year:"))
#
# books.append({
#     "name": nazov3,
#     "price": cena3,
#     "author": author3,
#     "publication_year": publication_year3,
# })
# print(f"{books[0]["name"]} , {books[0]["price"]} , {books[0]["author"]} , {books[0]["publication_year"]}")
# print(f"{books[1]["name"]} , {books[1]["price"]} , {books[1]["author"]} , {books[1]["publication_year"]}")
# print(f"{books[2]["name"]} , {books[2]["price"]} , {books[2]["author"]} , {books[2]["publication_year"]}")
#
# #Homework 2.(lesson 4)
# # Jednodušší úkol:
# # Vytvořte tři proměnné: věk kupujícího, jeho aktuální zůstatek peněz a cenu piva. Napište podmínku, která rozhodne, zda si uživatel může koupit pivo. Hodnoty všech proměnných můžete zadat v programu staticky, nebo je dynamicky přijmout z uživatelského vstupu. Pokud si uživatel může pivo koupit, vypiš jeho zůstatek peněz po nákupu.
# #
# # Pokud si pivo může koupit, vypište například:
# # "Můžeš si koupit pivo! Zůstatek peněz na účtu: 320Kč"
# # Pokud si ho koupit nemůže, vypište odpovídající zprávu, například:
# # "Nemůžeš si koupit pivo: nesplňuješ podmínky."
#
# vek = (input("Zadaj svoj vek:"))
#
# if vek.isdigit():
#     cislo = int(vek)
#     if cislo < 18:
#         print("Nemozes si kupit pivo,nie si plnolety.")
#         exit()
#     else:
#         print("Mozes si kupit pivo,si plnolety.")
# else:
#     print("Nezadal si cele cislo")
#
# cena_piva = (input("Zadaj cenu piva(Kc): "))
# if cena_piva.isdigit():
#     cena_piva = int(cena_piva)
# else:
#     print("Nezadal si cele cislo")
#     exit()
#
# zostatok = (input("Zadaj svoj zostatok(Kc):"))
# if zostatok.isdigit():
#     zostatok = int(zostatok)
# else:
#     print("Nezadal si cele cislo")
#     exit()
# if zostatok < cena_piva:
#         print("Nemozes si kupit pivo,nemas dostatok penazi.")
#
# else:
#     print("Mozes si kupit pivo.")

#homework 3(lesson5)
numbers = [1, 2, 4, -6, 7, 8, 100, -125, 11, 123]
names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
random_codes = ["1-okdsaaa", "0-nFnldd", "0-AA", "0-uwqqq", "2-ZSTh", "0-RKOcsxxx", "1-LwWtss", "0-cdKiddd", "2-KpAAaa", "3-sOdSxhcds"]

# 1. pomocí cyklu for vypište čísla ze seznamu numbers, ale přeskočte záporná čísla.

# 2. pomocí cyklu while vypište všechna jména, pokud narazíš na jméno 'Alice' cyklus ukonči

# 3. pomocí list comprehension vytvoř nový list, který bude obsahovat pouze prvky z 'random_codes', které obsahují 0

# Dobrovolny ukol pro pokrocile (nebude bodovan): Vypis všechny pod-seznamy s alespoň třemi po sobě jdoucími stejnými znaky v seznamu 'random_codes'

for num in numbers: #prejde vsetky polozky v zozname numbers a vytvori num
    if num < 0:
        continue #skoc na dalsie cislo ale nevypisuj
    print(num)

i = 0 #zaciatok na prvom indexe(index 0 = "Peter"
while i < len(names):
    if names[i] == "Alice":#narazi na Alice pouzije break a ukonci cyklus
        break
    print(names[i])
    i += 1

codes_with_zero = [code for code in random_codes if "0" in code]
print(codes_with_zero)






