import unittest
from EmotionDetection import emotion_detector as ed


class Test(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(
            ed("I am glad this happened")["dominant_emotion"],
            "joy"
        )

    def test_anger(self):
        self.assertEqual(
            ed("I am really mad about this")["dominant_emotion"],
            "anger"
        )

    def test_disgust(self):
        self.assertEqual(
            ed("I feel disgusted just hearing about this")["dominant_emotion"],
            "disgust"
        )

    def test_sadness(self):
        self.assertEqual(
            ed("I am so sad about this")["dominant_emotion"],
            "sadness"
        )

    def test_fear(self):
        self.assertEqual(
            ed("I am really afraid that this will happen")["dominant_emotion"],
            "fear"
        )


if __name__ == "__main__":
    unittest.main()