from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        result_joy_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_joy_1['dominant_emotion'], 'joy')

        result_anger_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_anger_1['dominant_emotion'], 'anger')

        result_disgust_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_disgust_1['dominant_emotion'], 'disgust')

        result_sadness_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_sadness_1['dominant_emotion'], 'sadness')

        result_fear_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_fear_1['dominant_emotion'], 'fear')

unittest.main()