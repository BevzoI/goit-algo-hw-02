import queue
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Лічильник для унікальних ID заявок
request_id_counter = 1

def generate_request():
    global request_id_counter
    request = f"Заявка #{request_id_counter}"
    request_queue.put(request)
    print(f"[+] Створено: {request}")
    request_id_counter += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[~] Обробка: {request}")
        # Імітація часу обробки заявки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[✓] Завершено: {request}")
    else:
        print("[!] Черга пуста. Немає заявок для обробки.")

def main():
    print("Сервісний центр запущено. Натисніть Ctrl+C для виходу.\n")
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 1.5))  # Імітація паузи між заявками
            process_request()
            print("-" * 40)
            time.sleep(random.uniform(0.5, 1.0))  # Коротка пауза перед наступним циклом
    except KeyboardInterrupt:
        print("\n[!] Завершення програми. До побачення!")

if __name__ == "__main__":
    main()
