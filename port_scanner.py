import socket

print("===== PYTHON PORT SCANNER =====")

# Scan only your own computer.
target = "127.0.0.1"

print("Scanning your own computer:", target)

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)

    result = s.connect_ex((target, port))

    if result == 0:
        print("Port", port, "is OPEN")

    s.close()

print("===== SCANNING COMPLETED =====")
