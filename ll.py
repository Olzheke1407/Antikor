import Antikor 

queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]


if Antikor.p(queens):
    print("Ферзи не бьют друг друга")
else:
    print("Ферзи бьют друг друга")