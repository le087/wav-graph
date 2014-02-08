#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Library for parsing wave-files."""


import wave
import math
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
        - `m`: режим, в котором открывается wav-файл
        """
        # ------ Данные, с парсенные из файла
        wav = wave.open(wavfile, mode=m)
        self.nchannels = wav.getnchannels()
        self.sampwidth = wav.getsampwidth()
        self.framerate = wav.getframerate()
        self.nframes = wav.getnframes()
        self.comptype = wav.getcomptype()
        self.compname = wav.getcompname()
        self.content = wav.readframes(self.nframes)

        # ------ Базовые составляющие для графиков
        self.duration = self.nframes / self.framerate
        self.width = 800
        self.heigh = 300
        self.dpi = 72
        self.peak = 256 ** self.sampwidth / 2
        self.koef = self.nframes / self.width / 2

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

    def format_time(self, x, pos=None):
        """По заданной координате возвращает время, где
        координата находится.

        - `x`: координата
        - `pos: неведомая вещь`
        """
        progress = int(x / float(self.nframes) * self.duration * self.koef)
        mins, secs = divmod(progress, 60)
        hours, mins = divmod(mins, 60)
        out = "%d:%02d" % (mins, secs)
        if hours > 0:
            out = "%d:" % hours
        return out

    def format_db(self, x, pos=None):
        """Возвращает текущую амплитуду в дицибелах
        
        - `x`: координата
        - `pos`: значение по вертикали
        """
        if pos == 0:
            return ""
        if x == 0:
            return "-inf"

        db = 20 * math.log10(abs(x) / float(self.peak))
        return int(db)

    def drawWave(self):
        """Просто рисует волну

        Arguments:
        - `self`: инстантс
        """

        plt.figure(1, figsize=(
            float(self.width)/self.dpi,
            float(self.heigh)/self.dpi),
            dpi=self.dpi)

        plt.subplots_adjust(wspace=0, hspace=0)

        for n in range(self.nchannels):
            channel = self.getarraysamples()[n::self.nchannels]

            channel = channel[0::self.koef]
            if self.nchannels == 1:
                channel = channel - self.peak

            axes = plt.subplot(2, 1, n+1, axisbg="k")
            axes.plot(channel, "g")
            axes.yaxis.set_major_formatter(ticker.FuncFormatter(self.format_db))
            plt.grid(True, color="w")
            axes.xaxis.set_major_formatter(ticker.NullFormatter())

        axes.xaxis.set_major_formatter(ticker.FuncFormatter(self.format_time))
        plt.savefig("rezult_images", dpi=self.dpi)
        plt.show()
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
    """ Тестовый прогон сия программулины
    """
    test = WaveGraph("tests/test.wav")
    test.drawWave()


if __name__ == '__main__':
    main()
