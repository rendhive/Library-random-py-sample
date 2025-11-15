import random

choices = ['apple', 'banana', 'cherry']
weights = [0.1, 0.3, 0.6]  # Probabilitas pemilihan
weighted_choice = random.choices(choices, weights=weights, k=5)
print("Pilihan berdasarkan probabilitas:", weighted_choice)
# Fungsi: Memilih elemen dengan probabilitas yang telah ditetapkan.
# Kondisi: Ketika Anda ingin memilih item dengan pengaruh probabilitas tertentu.
