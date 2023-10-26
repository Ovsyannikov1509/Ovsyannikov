# TODO Найдите количество книг, которое можно разместить на дискете
volume_in_bites = 1.44 * 1024 * 1024
symbols = 25
lines = 50
pages = 100
bites_in_symbol = 4
book_in_bites = symbols * lines * pages * bites_in_symbol
books_on_disk = int(volume_in_bites // book_in_bites)
print("Количество книг, помещающихся на дискету:", books_on_disk)
