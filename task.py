from queue import Queue
import random
import time
import datetime

# Створити чергу заявок
request_queue = Queue()

# Лічильник для унікальних ID заявок
request_id_counter = 1

def generate_request():
    global request_id_counter
    new_request = {
        'id': request_id_counter,
        'created_at': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    request_queue.put(new_request)
    print(f"[+] Створено: Заявка #{new_request['id']} о {new_request['created_at']}")
    request_id_counter += 1

def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[~] Обробка: Заявка #{request['id']} (створена о {request['created_at']})")
        time.sleep(random.uniform(0.5, 1.5))  # Імітація часу обробки
        print(f"[✓] Завершено: Заявка #{request['id']}\n")
    else:
        print("[!] Черга пуста. Немає заявок для обробки.\n")

def main():
    print("Сервісний центр запущено. Введіть 'exit' для виходу.\n")
    
    while True:
        generate_request()
        time.sleep(random.uniform(0.3, 1.0))  # Затримка між генерацією і обробкою
        process_request()

        # Перевірка на вихід
        user_input = input("Натисніть Enter для продовження або введіть 'exit' для виходу: ")
        if user_input.strip().lower() == 'exit':
            print("\n[!] Завершення програми. До побачення!")
            break
        print("-" * 50)

if __name__ == "__main__":
    main()
