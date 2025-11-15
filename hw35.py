"""
=======================================
 ЗАДАНИЕ 1. МАТЕМАТИЧЕСКИЕ ВЫЧИСЛЕНИЯ
=======================================
Нужно:
1) Реализовать heavy_math(x) — "тяжёлая" функция (CPU-bound).
   Например: число Фибоначчи, факториал, интеграл и т.п.
2) Написать три варианта:
   - Последовательно
   - В потоках
   - В процессах
3) Замерить время и сравнить.
"""

import time
import threading
from multiprocessing import Process
import requests
from functools import wraps


# ---------------------------
# Декоратор замера времени
# ---------------------------
def measure_time(label=""):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{label} {end - start:.2f} сек")
            return result
        return wrapper
    return decorator


# ---------------------------
# Общая функция для математики
# ---------------------------


def heavy_math(x):
    """
    TODO: Реализовать "тяжёлую" математическую задачу.
    Например: рекурсивный fib(n), факториал через цикл и т.п.
    """
    s = 0
    y = x * 300000 + 2000000
    for i in range(y):
        s += i
    return s
      
# ---------------------------
# 1. Последовательный вариант
# ---------------------------
@measure_time("[Математика] Последовательно:")
def math_sequential(N=5):
    for i in range(N):
        result = heavy_math(i)
        print(f"Результат {i}: {result}")


# ---------------------------
# 2. Потоки
# ---------------------------
@measure_time("[Математика] Потоки:")
def math_threads(N=5):
    def worker(x):
        result = heavy_math(x)
        print(f"[Поток {x}] → {result}")

    threads = []
    for i in range(N):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# ---------------------------
# 3. Процессы
# ---------------------------
def math_worker(x):
    result = heavy_math(x)
    print(f"[Процесс {x}] → {result}")

@measure_time("[Математика] Процессы:")
def math_processes(N=5):
    processes = []
    for i in range(N):
        p = Process(target=math_worker, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


"""
=======================================
 ЗАДАНИЕ 2. GET-ЗАПРОСЫ
=======================================
Нужно:
1) Реализовать fetch_url(url), который делает GET-запрос.
2) Написать три варианта:
   - Последовательно
   - В потоках
   - В процессах
3) Замерить время и сравнить.
"""

# ---------------------------
# Общая функция для запросов
# ---------------------------
def fetch_url(url):
    """
    TODO: Реализовать GET-запрос через requests.get(url).
    Вернуть, например, status_code.
    """
    response = requests.get(url, timeout=10)
    return response.status_code
    


# ---------------------------
# 1. Последовательный вариант
# ---------------------------
@measure_time("[GET] Последовательно:")
def net_sequential(urls):
    for url in urls:
        result = fetch_url(url)
    print(f"{url} → {result}")


# ---------------------------
# 2. Потоки
# ---------------------------
@measure_time("[GET] Потоки:")
def net_threads(urls):
    def worker(url):
        result = fetch_url(url)
        print(f"[Поток] {url} → {result}")

    threads = []
    for url in urls:
        t = threading.Thread(target=worker, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


# ---------------------------
# 3. Процессы
# ---------------------------
def worker(url):
    result = fetch_url(url)
    print(f"[Процесс] {url} → {result}")
@measure_time("[GET] Процессы:")
def net_processes(urls):
    processes = []
    for url in urls:
        p = Process(target=worker, args=(url,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


"""
=======================================
 ЗАПУСК ТЕСТОВ
=======================================
"""

if __name__ == "__main__":
    # Задание 1: математика
    print("\n=== ЗАДАНИЕ 1: МАТЕМАТИКА ===")
    math_sequential(N=5)
    math_threads(N=5)
    math_processes(N=5)

    # Задание 2: GET-запросы
    print("\n=== ЗАДАНИЕ 2: GET-ЗАПРОСЫ ===")
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/3",
    ]
    net_sequential(urls)
    net_threads(urls)
    net_processes(urls)