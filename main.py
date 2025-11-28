def trim_and_repeat(text: str, offset: int = 0, repetitions: int = 1) -> str:
    trimmed_text = text[offset:]
    result = trimmed_text * repetitions
    return result


# Пример:
# print(trim_and_repeat("hello"))  # -> "hello"
# print(trim_and_repeat("hello", 2))  # -> "llo"
# print(trim_and_repeat("hello", 1, 3))  # -> "ellhellhell"
