import random
import sys
import time

sys.setrecursionlimit(200000)

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j]["id"] > a[j + 1]["id"]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j]["id"] < a[min_idx]["id"]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]["id"]
    left = [x for x in arr if x["id"] < pivot]
    middle = [x for x in arr if x["id"] == pivot]
    right = [x for x in arr if x["id"] > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# ЧАСТЬ 2: Анализ логов


def counting_sort_by_status(logs):
    buckets = [[] for _ in range(600)]
    for log in logs:
        buckets[log["status"]].append(log)

    sorted_logs = []
    for bucket in buckets:
        if bucket:
            sorted_logs.extend(bucket)
    return sorted_logs


def radix_sort_by_ip(logs):
    result = logs.copy()
    for byte_index in (3, 2, 1, 0):
        buckets = [[] for _ in range(256)]
        for item in result:
            octet = int(item["ip"].split(".")[byte_index])
            buckets[octet].append(item)
        result = []
        for bucket in buckets:
            result.extend(bucket)
    return result

# ЗАПУСК, ЗАМЕРЫ И РАСПИСАННЫЙ ОТЧЕТ

if __name__ == "__main__":
    names = [
        "Ноутбук",
        "Мышь",
        "Клавиатура",
        "Монитор",
        "Кабель",
        "Наушники",
    ]
    TEST_SIZE = 2000

    print(f"Генерация {TEST_SIZE} товаров для базовых тестов...")
    products = [
        {"id": random.randint(1, 1000000), "name": random.choice(names)}
        for _ in range(TEST_SIZE)
    ]

    t0 = time.perf_counter()
    bubble_sort(products)
    t_bubble = time.perf_counter() - t0

    t0 = time.perf_counter()
    selection_sort(products)
    t_select = time.perf_counter() - t0

    t0 = time.perf_counter()
    quick_sort(products)
    t_quick = time.perf_counter() - t0

    print("\n" + "=" * 50)
    print("ИТОГОВАЯ ТАБЛИЦА СКОРОСТИ (ЧАСТЬ 1: ТОВАРЫ)")
    print("=" * 50)
    print(f"{'Алгоритм':<20} | {'Элементов':<10} | {'Время (сек)':<12}")
    print("-" * 50)
    print(f"{'Bubble Sort':<20} | {TEST_SIZE:<10} | {t_bubble:.4f}")
    print(f"{'Selection Sort':<20} | {TEST_SIZE:<10} | {t_select:.4f}")
    print(f"{'Quick Sort':<20} | {TEST_SIZE:<10} | {t_quick:.4f}")

    #  Часть 2: Сетевые логи (DDoS анализ)
    TOTAL_LOGS = 10000
    print("\n" + "=" * 50)
    print(f"ГЕНЕРАЦИЯ И ОБРАБОТКА {TOTAL_LOGS} ЛОГОВ (ЧАСТЬ 2)")
    print("=" * 50)

    sample_ips = [
        f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
        for _ in range(30)
    ]
    status_codes = [200, 201, 301, 400, 403, 404, 500, 502, 503]

    traffic_logs = [
        {
            "ip": random.choice(sample_ips),
            "status": random.choice(status_codes),
            "url": "/api/v1/products",
        }
        for _ in range(TOTAL_LOGS)
    ]

    # 1. Counting Sort
    t0 = time.perf_counter()
    sorted_by_status = counting_sort_by_status(traffic_logs)
    t_status = time.perf_counter() - t0

    # 2. Radix Sort
    t0 = time.perf_counter()
    sorted_by_ip = radix_sort_by_ip(traffic_logs)
    t_ip = time.perf_counter() - t0

    # Подсчет статистики распределения кодов
    status_counts = {}
    for entry in sorted_by_status:
        st = entry["status"]
        status_counts[st] = status_counts.get(st, 0) + 1

    # Подсчет запросов с уникальных IP
    ip_counts = {}
    for entry in sorted_by_ip:
        ip = entry["ip"]
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
    top_attackers = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[
        :3
    ]

    print("\n[1] РЕЗУЛЬТАТ COUNTING SORT (Сортировка по HTTP-статусам):")
    print(f"-> Время обработки: {t_status:.4f} сек")
    print("-> Распределение логов по корзинам (статусам):")
    for code, count in sorted(status_counts.items()):
        print(f"    Код {code}: {count} запросов")

    print("\n[2] РЕЗУЛЬТАТ RADIX SORT (Поразрядная сортировка по IPv4):")
    print(f"-> Время обработки: {t_ip:.4f} сек")
    print("-> Пример упорядоченных IP (первые 5 записей):")
    for row in sorted_by_ip[:5]:
        print(f"    IP: {row['ip']:<15} | Status: {row['status']}")

    print("\n[3] АНАЛИЗ БЕЗОПАСНОСТИ (Выявление аномалий):")
    print("-> Топ-3 IP-адреса с наибольшей активностью:")
    for ip, count in top_attackers:
        percent = (count / TOTAL_LOGS) * 100
        print(f"    IP {ip:<15} -> {count} запросов ({percent:.1f}% трафика)")
    print("=" * 50)