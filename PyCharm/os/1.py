#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Скачали календарь на февраль, март и апрель, но файлы были названы February.png, April.png и April(1).png.
Нужно переименовать April в March, а April(1) в April, чтобы не путаться в месяцах.
Так как февраль уже прошел, решили что хранение изображения календаря на февраль - не нужно.
Следует удалить February.png.
В процессе работы запутались в каталогах, нужно определить текущий.
"""

import os

if __name__ == "__main__":
    os.rename("April.png", "March.png")
    os.rename("April(1).png", "April.png")
    os.remove("February.png")
    path = os.getcwd()
    print(path)
