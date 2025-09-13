
import unittest
import json
from video_processor import VideoProcessor, VideoObject, Frame, AnalysisResults

class TestVideoProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = VideoProcessor()
        self.video = self.processor.load_video('video/test_video.mp4')
        self.frames = self.processor.extract_frames(self.video, 'fixed_interval', {'interval': 10})

    def test_load_video(self):
        self.assertIsInstance(self.video, VideoObject)
        self.assertEqual(self.video.path, 'video/test_video.mp4')

    def test_extract_frames(self):
        self.assertGreater(len(self.frames), 0)
        self.assertIsInstance(self.frames[0], Frame)

    def test_analyze_features(self):
        results = self.processor.analyze_features(self.frames)
        self.assertIsInstance(results, AnalysisResults)
        self.assertIn('total_frames', results.features)

    def test_save_results(self):
        results = self.processor.analyze_features(self.frames)
        self.processor.save_results(results, 'results/test_results.json')
        with open('results/test_results.json', 'r') as f:
            saved_results = json.load(f)
        # self.assertEqual(saved_results, results.features)

if __name__ == "__main__":
    unittest.main()
    