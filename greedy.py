
# Data tugas
jobs = [
          {"id": "A", "deadline": 2, "profit": 100},
          {"id": "B", "deadline": 1, "profit": 19},
          {"id": "C", "deadline": 2, "profit": 27},
          {"id": "D", "deadline": 1, "profit": 25},
          {"id": "E", "deadline": 3, "profit": 15}
]

# 1. Urutkan berdasarkan profit terbesar
jobs.sort(key=lambda x: x["profit"], reverse=True)

# 2. Tentukan jumlah slot waktu
max_deadline = max(job["deadline"] for job in jobs)
slots = [None] * max_deadline

total_profit = 0

# 3. Proses Greedy
print("="*50)
print(f"{"List Tugas yang Diproses:".upper().center(50)}")
print("="*50)
for job in jobs:
          print(job)
          # Cari slot kosong dari deadline terbesar
          # menuju slot pertama
          for slot in range(job["deadline"] - 1, -1, -1):
                    if slots[slot] is None:
                              slots[slot] = job
                              total_profit += job["profit"]
                              break
print("="*50)
print("\n")

# 4. Tampilkan hasil
print("="*30)
print(f"{"Jadwal Tugas:".upper().center(30)}")
print("="*30)
for i, job in enumerate(slots):
          if job is not None:
                    print(
                    f"Slot {i+1}: Tugas {job['id']} "
                    f"(Profit: {job['profit']})"
                    )
          else:
                    print(f"Slot {i+1}: Kosong")

print("Total Profit:", total_profit)
print("="*30)
