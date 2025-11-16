import random

numbers = [random.randint(1, 100) for _ in range(10)]
average = sum(numbers) / len(numbers)
print("Rata-rata dari bilangan acak:", average)
# Fungsi: Menghitung rata-rata dari sekumpulan bilangan acak.
# Kondisi: Ketika Anda perlu menganalisis data acak.
