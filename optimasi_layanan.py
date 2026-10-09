"""Mencari kombinasi paket layanan dengan keuntungan maksimum.

Model:
    Maksimalkan Z = 12x + 10y (juta rupiah)
    dengan 4x + 2y <= 40 (jam konsultan senior)
         2x + 3y <= 36 (jam konsultan junior)
         x, y >= 0

Skrip ini memeriksa solusi bilangan bulat karena jumlah paket harus utuh.
"""

best = None
for penetration_testing in range(41):
    for security_audit in range(37):
        senior_hours = 4 * penetration_testing + 2 * security_audit
        junior_hours = 2 * penetration_testing + 3 * security_audit
        if senior_hours <= 40 and junior_hours <= 36:
            profit = 12_000_000 * penetration_testing + 10_000_000 * security_audit
            candidate = (profit, penetration_testing, security_audit, senior_hours, junior_hours)
            if best is None or candidate[0] > best[0]:
                best = candidate

profit, penetration_testing, security_audit, senior_hours, junior_hours = best
print("Kombinasi optimal:")
print(f"Penetration Testing : {penetration_testing} paket")
print(f"Security Audit      : {security_audit} paket")
print(f"Jam konsultan senior: {senior_hours} dari 40 jam")
print(f"Jam konsultan junior: {junior_hours} dari 36 jam")
print(f"Keuntungan maksimum: Rp{profit:,.0f}".replace(",", "."))
