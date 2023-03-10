#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Написать программу, которая считывает английский текст из файла и выводит на экран
слова текста, начинающиеся и оканчивающиеся на гласные буквы."""

def s(text):
    lts = 'ueioay'
    for word in text:
        words = []
        for prword in lts:
            if word[0] == prword:
                words = str(lts)
        for prword in words:
            if word.endswith(prword):
                print(word)


if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()
    text = str(sentences).lower().split()
    s(text)

