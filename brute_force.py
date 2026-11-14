
from itertools import combinations

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

best_profit = 0
best_jobs = []

# 1. Coba seluruh kombinasi tugas
for r in range(len(jobs) + 1):
    for selected in combinations(jobs, r):

        # 2. Urutkan berdasarkan deadline terkecil
        ordered = sorted(
            selected,
            key=lambda x: x["deadline"]
        )

        # 3. Periksa apakah kombinasi memenuhi deadline
        feasible = True

        for i, job in enumerate(ordered):
            if i + 1 > job["deadline"]:
                feasible = False
                break

        # 4. Hitung profit kombinasi yang valid
        if feasible:
            profit = sum(
                job["profit"] for job in ordered
            )

            # 5. Simpan kombinasi dengan profit terbesar
            if profit > best_profit:
                best_profit = profit
                best_jobs = ordered

# 6. Tampilkan hasil
print("=" * 35)
print("HASIL BRUTE FORCE".center(35))
print("=" * 35)

for i, job in enumerate(best_jobs):
    print(
        f"Slot {i+1}: Tugas {job['id']} "
        f"(Profit: {job['profit']})"
    )

print("-" * 35)
print("Total Profit:", best_profit)
print("=" * 35)
