id_tugas = [str(input("Masukkan ID tugas 1: ")), str(input("Masukkan ID tugas 2: ")), str(input("Masukkan ID tugas 3: ")), str(input("Masukkan ID tugas 4: ")), str(input("Masukkan ID tugas 5: "))]

deadline_tugas = [int(input("Masukkan deadline tugas 1: ")), int(input("Masukkan deadline tugas 2: ")), int(input("Masukkan deadline tugas 3: ")), int(input("Masukkan deadline tugas 4: ")), int(input("Masukkan deadline tugas 5: "))]

profit_tugas = [int(input("Masukkan profit tugas 1: ")), int(input("Masukkan profit tugas 2: ")), int(input("Masukkan profit tugas 3: ")), int(input("Masukkan profit tugas 4: ")), int(input("Masukkan profit tugas 5: "))]

# Data tugas
jobs = [
          {"id": id_tugas[0], "deadline": deadline_tugas[0], "profit": profit_tugas[0]},
          {"id": id_tugas[1], "deadline": deadline_tugas[1], "profit": profit_tugas[1]},
          {"id": id_tugas[2], "deadline": deadline_tugas[2], "profit": profit_tugas[2]},
          {"id": id_tugas[3], "deadline": deadline_tugas[3], "profit": profit_tugas[3]},
          {"id": id_tugas[4], "deadline": deadline_tugas[4], "profit": profit_tugas[4]}
]
print("\n")

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
