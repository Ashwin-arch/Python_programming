import socket

def scan_ports(target_ip, ports=[21, 22, 23, 25, 53, 80, 443, 8080]):
    open_ports = []

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            if result == 0:
                open_ports.append(port)
            s.close()
        except Exception:
            pass

    return open_ports
