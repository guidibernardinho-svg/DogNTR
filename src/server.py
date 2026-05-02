import socket
import json
import threading

# =========================
# LOAD CONFIG
# =========================
with open("config.json", "r") as f:
    config = json.load(f)

VIDEO_PORT = config.get("video_port", 8000)
INPUT_PORT = config.get("input_port", 9000)

# =========================
# VIDEO STREAM HANDLER
# =========================
def handle_video_stream():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", VIDEO_PORT))
    server.listen(1)

    print(f"🎥 Video server running on port {VIDEO_PORT}")

    conn, addr = server.accept()
    print("📡 Video connected:", addr)

    while True:
        try:
            data = conn.recv(65536)
            if not data:
                break

            # aqui futuramente: decode frame (JPEG / RAW)
            print(f"🎞️ Frame received: {len(data)} bytes")

        except Exception as e:
            print("❌ Video error:", e)
            break

    conn.close()


# =========================
# INPUT STREAM HANDLER
# =========================
def handle_input_stream():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", INPUT_PORT))

    print(f"🎮 Input server running on port {INPUT_PORT}")

    while True:
        try:
            data, addr = server.recvfrom(1024)
            msg = data.decode()

            # exemplo: A:DOWN | STICK:120:80
            print(f"🎮 Input from {addr}: {msg}")

        except Exception as e:
            print("❌ Input error:", e)
            break


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("🚀 DogNTR Server starting...")

    video_thread = threading.Thread(target=handle_video_stream)
    input_thread = threading.Thread(target=handle_input_stream)

    video_thread.start()
    input_thread.start()

    video_thread.join()
    input_thread.join()
