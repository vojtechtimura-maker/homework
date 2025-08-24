# # Cvičení: List comprehension v Pythonu
# # ------------------------------------
# # Tvým úkolem je přepsat klasický zápis (s for cyklem) do list comprehension.
#
# # Úloha 1: Vytvoř seznam druhých mocnin čísel od 0 do 9
# squares = []
# for n in range(10):
#     squares.append(n ** 2)
#
# # Přepiš sem jako list comprehension:
# squares = [ n**2 for n in range(10) ]
# print(squares)
#
#
# # ------------------------------------
# # Úloha 2: Vytvoř seznam slov kratších než nebo rovna 4 znakům
# words = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
# short_words = []
# for w in words:
#     if len(w) <= 4:
#         short_words.append(w)
#
# # Přepiš sem jako list comprehension:
#
# short_words = [ w for w in words if len(w) <= 4 ]
# print(short_words)
#
# # ------------------------------------
# # Úloha 3: Vytvoř seznam druhých mocnin lichých čísel
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_squares = []
# for n in numbers:
#     if n % 2 == 1:
#         odd_squares.append(n ** 2)
#
# # Přepiš sem jako list comprehension:
# odd_squares = [ n**2 for n in range(10) if n % 2 == 1 ]
# print(odd_squares)
#
# # ------------------------------------
# # Úloha 4 (bonus): Najdi všechna slova, která začínají na písmeno 'A'
# names = ["Petr", "Ales", "Honza", "Lenka", "Andrea", "Alice"]
# names_with_a = []
# for name in names:
#     if name.startswith("A"):
#         names_with_a.append(name)
#
# # Přepiš sem jako list comprehension:
# names_with_a = [ name for name in names if name.startswith("A") ]
# print(names_with_a)