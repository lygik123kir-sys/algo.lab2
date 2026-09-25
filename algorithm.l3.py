#A:
def is_subset(larger, smaller):
    #
    lookup_set = set(larger)


    for item in smaller:
        if item not in lookup_set:
            return False

    return True



list1 = ["a", "b", "c", "d", "e", "f"]
list2 = ["b", "d", "f"]
print(is_subset(list1, list2))

list3 = ["b", "d", "f", "h"]
print(is_subset(list1, list3))


#B

# def first_unique_char(s):
#
#     char_counts = {}
#
#     for char in s:
#         char_counts[char] = char_counts.get(char, 0) + 1
#
#     for char in s:
#         if char_counts[char] == 1:
#             return char
#
#     return None
#
# word = "minimum"
# print(first_unique_char(word))


#C

# def longest_palindrome(s):
#
#     counts = {}
#     for char in s:
#         counts[char] = counts.get(char, 0) + 1
#
#     max_length = 0
#     has_odd = False
#
#
#     for count in counts.values():
#         max_length += (count // 2) * 2
#         if count % 2 == 1:
#             has_odd = True
#
#
#     if has_odd:
#         max_length += 1
#
#     return max_length
#
# tests_c = [
#     ("aAbBABba", 8),
#     ("abcdefghijklmnoPQrstuvwxyz", 1),
#     ("wasitacaroracatisaw", 19),
#     ("bbbabab", 7),
#     ("abcdeedcba", 10),
#     ("looooooongestpalindrOme", 13),
#     ("abcdeedcbaxyz", 11),
#     ("abbbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbabbab" ,1122
# )]
#
# for string, expected in tests_c:
#     result = longest_palindrome(string)
#
#     display_str = string if len(string) <= 30 else string[:20] + "...(длина " + str(len(string)) + ")"
#     print(f"Тест: '{display_str}' -> Получено: {result} | Ожидалось: {expected} | Статус: {'OK' if result == expected else 'ОШИБКА'}")
#     assert result == expected, f"Ошибка на тесте {display_str}!"

#D

# def is_anagram(s, t):
#
#     if len(s) != len(t):
#         return False
#
#
#     count_s = {}
#     count_t = {}
#
#     for char in s:
#         count_s[char] = count_s.get(char, 0) + 1
#
#     for char in t:
#         count_t[char] = count_t.get(char, 0) + 1
#
#
#     return count_s == count_t
#
#
#
# tests_d = [
#     ("нора", "рано", True),
#     ("монета", "отмена", True),
#     ("мышка", "камыш", True),
#     ("тормони", "монитор", True),
#     ("тоемони", "монитор", False),
#     ("анаграмма", "амгармана", True),
#     ("анаграмма", "грамм", False),
# ]
#
# for s_str, t_str, expected in tests_d:
#     res = is_anagram(s_str, t_str)
#     status = "OK" if res == expected else "ОШИБКА"
#     print(f"Строки: '{s_str}' и '{t_str}' -> Результат: {res} (Ожидалось: {expected}) | Статус: {status}")
#     assert res == expected, f"Ошибка на {s_str}, {t_str}!"