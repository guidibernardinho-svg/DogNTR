import socket

def start_stream(port=8000):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(1)

    print("🎥 Waiting for 3DS stream...")

    conn, addr = server.accept()
    print("Connected:", addr)

    while True:
        data = conn.recv(65536)
        if not data:
            break

        # aqui depois você decodifica imagem (JPEG/RAW)
        print("Frame received:", len(data))
