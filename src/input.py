import socket

class InputClient:
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addr = (ip, port)

    def send_button(self, button, state):
        msg = f"{button}:{'DOWN' if state else 'UP'}"
        self.sock.sendto(msg.encode(), self.addr)

    def send_stick(self, x, y):
        msg = f"STICK:{x}:{y}"
        self.sock.sendto(msg.encode(), self.addr)
