#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
import wav_graph


class TestWaveParse(unittest.TestCase):

    def setUp(self):
        self.wave = wav_graph.WaveGraph("test.wav")

    def testReadWave(self):
        self.assertEqual(self.wave.nchannels, 2)
        self.assertEqual(self.wave.sampwidth, 2)
        self.assertEqual(self.wave.framerate, 44100)
        self.assertEqual(self.wave.nframes, 188806)
        self.assertEqual(self.wave.comptype, "NONE")
        self.assertEqual(self.wave.compname, "not compressed")

    def testPrintInfo(self):
        self.assertEqual(self.wave.info("test.wav"), True)


if __name__ == '__main__':
    unittest.main()
