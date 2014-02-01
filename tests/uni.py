#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath(".."))

#import md5
import unittest
import wav_graph


class TestWaveParse(unittest.TestCase):

    def setUp(self):
        self.wave = wav_graph.WaveParse("test.wav")

    def testReadWave(self):
        self.assertEqual(self.wave.nchanels, 2)
        self.assertEqual(self.wave.sampwidth, 2)
        self.assertEqual(self.wave.framerate, 44100)
        self.assertEqual(self.wave.nframes, 188806)
        self.assertEqual(self.wave.comptype, "NONE")
        self.assertEqual(self.wave.compname, "not compressed")
        # self.assertEqual(md5.md5.hexdigest(self.wave.content), "hash")


if __name__ == '__main__':
    unittest.main()
