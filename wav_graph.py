#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Library for parsing wave-files."""


import wave


class WaveParse(object):
    """Объект предназначен для парсинга wave-файлов и
    содержит информацию о спарсенном файле.
    """

    def __init__(self, filename):
        """Напишу чего-нибудь позже

        Arguments:
        - `filename`: путь до файла
        """
        self.filename = filename
        (self.nchanels, self.sampwidth,
         self.framerate, self.nframes,
         self.comptype, self.compname) = self.getparams()

    def getparams(self):
        """Возвращает параметры wave файла
        """
        wave_inst = wave.open(self.filename)
        return wave_inst.getparams()

    def getcontent(self):
        """Возвращает содержимое wave.
        Arguments:
        - `self`:
        """
        return wave.open(self.filename)


class WaveGraph(object):
    """Рисует различные графики, применяет фильтры.
    """

    def __init__(self, waveparse):
        """Первоначально мы выполняем действия только
        для отрисовки волны.

        Arguments:
        - `waveparse`: инстанс класса WaveParse
        """
        self.waveparse = waveparse

    def drawWave(self):
        """Просто рисует волну

        Arguments:
        - `self`:
        """
        return 0

    def drawFR(self):
        """Рисует АЧХ
        """
        return 0

    def drawRectangle(self):
        """Цифровой полосовй фильтр прямоуголное окно
        """
        return 0

    def drawHemming(self):
        """Цифровой полосовой фильт окно Хемминга
        """
        return 0


def main():
    """
    """
    pass


if __name__ == '__main__':
    main()
