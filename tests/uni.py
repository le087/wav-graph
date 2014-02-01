#!/usr/bin/python
# -*- coding: utf-8 -*-


import unittest
import wav_graph


class TestWaveParse(unittest.TestCase):

    def setUp(self):
        self.filename = wav_graph.WaveParse("test.wav")

    def testReadWave(self):
        pass


if __name__ == '__main__':
    unittest.main()
