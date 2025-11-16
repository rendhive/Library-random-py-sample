import random

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = random.sample(list1 + list2, 4)  # Mengambil 4 elemen acak dari gabungan dua list
print("Gabungan dua list secara acak:", combined_list)
# Fungsi: Menggabungkan dua list dan mengambil elemen acak tanpa mengganti.
# Kondisi: Ketika Anda ingin memiliki kombinasi acak dari dua sumber data.
