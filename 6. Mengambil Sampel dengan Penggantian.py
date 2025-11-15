import random

my_list = [1, 2, 3]
sample_with_replacement = random.choices(my_list, k=2)  # Mengambil 2 elemen acak dengan penggantian
print("Sampel dengan penggantian:", sample_with_replacement)
# Fungsi: Mengambil elemen acak dari kumpulan dengan kemungkinan pengulangan.
# Kondisi: Ketika Anda perlu mengizinkan pengulangan dalam sampling.
