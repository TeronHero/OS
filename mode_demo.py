import os

print("=== User Mode vs Kernel Mode ===\n")

print("-- ma dar User Mode hastim --")
print(f"PID barnameye ma: {os.getpid()}")
print(f"karbaro feli: {os.getlogin()}")

print("\n-- darkhaast az Kernel (System Call) --")
print("dar hale khandan fayl...")

with open("/etc/hostname", "r") as f:
    hostname = f.read().strip()

print(f"Kernel javab dad: hostname = {hostname}")

print("\n-- bargashtim be User Mode --")
print("System Call tamoom shod!")
