#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Library for parsing wave-files."""


class WaveParse(object):
    """Объект предназначен для парсинга wave-файлов и
    содержит информацию о спарсенном файле.
    """

    def __init__(self, filename):
        """Напишу чего-нибудь позже

        Arguments:
        - `filename`: путь до файла
        """
        self._filename = filename


class WaveGraph(object):
    """Рисует различные графики, применяет фильтры.
    """

    def __init__(self, waveparse):
        """Первоначально мы выполняем действия только
        для отрисовки волны.

        Arguments:
        - `waveparse`: инстанс класса WaveParse
        """
        self._waveparse = waveparse


def main():
    """
    """
    pass


if __name__ == '__main__':
    main()
