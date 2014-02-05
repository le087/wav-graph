#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Library for parsing wave-files."""


import wave
import numpy
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class WaveGraph(object):
    """Рисует различные графики, применяет фильтры.
    """

    def __init__(self, wavfile, m='r'):
        """Первоначально мы выполняем действия только
        для отрисовки волны.

        Arguments:
        - `wavfile`: инстанс класса Wavfile
        """
        wav = wave.open(wavfile, mode=m)
        self.nchannels = wav.getnchannels()
        self.sampwidth = wav.getsampwidth()
        self.framerate = wav.getframerate()
        self.nframes = wav.getnframes()
        self.comptype = wav.getcomptype()
        self.compname = wav.getcompname()
        self.content = wav.readframes(self.nframes)

    def info(self, wavfile):
        """Показывает собранную информацию о wav-файле.
        """
        info = """        Информация о wave:
        ===================================
        Имя файла: {0}
        Число каналов: {1}
        Байт/сэмпл: {2}
        Фрейм/сек: {3}
        Всего фреймов: {4}
        """.format(wavfile, self.nchannels,
                   self.sampwidth, self.framerate,
                   self.nframes)
        print(info)
        return True

    def getarraysamples(self):
        """Возваращает массив из спарсеного в строке потока
        """
        types = {
            1: numpy.int8,
            2: numpy.int16,
            3: numpy.int32
        }
        return numpy.fromstring(self.content, dtype=types[self.sampwidth])

    def drawWave(self):
        """Просто рисует волну

        Arguments:
        - `self`:
        """
        for n in range(self.nchanels):
            channel = getarraysamples()[n::self.nchannels]

        
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
