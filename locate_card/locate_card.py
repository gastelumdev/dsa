import unittest

class TestCases(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0], 7), 3)

    def test_case2(self):
        self.assertEqual(locate_card([13, 11, 10, 7, 4, 3, 1, 0], 1), 6)

    def test_case3(self):
        self.assertEqual(locate_card([4, 2, 1, -1], 4), 0)

    def test_case4(self):
        self.assertEqual(locate_card( [3, -1, -9, -127], -127), 3)

    def test_case5(self):
        self.assertEqual(locate_card([6], 6), 0)

    def test_case6(self):
        self.assertEqual(locate_card([9, 7, 5, 2, -9], 4), -1)

    def test_case7(self):
        self.assertEqual(locate_card([], 7), -1)

    def test_case8(self):
        self.assertEqual(locate_card([8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 3), 7)

    def test_case9(self):
        self.assertEqual(locate_card([8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 6), 2)

    

def locate_card(cards, query):
    position = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        
        position += 1

    return -1
        


tests = []

tests.append({'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3})
tests.append({'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6})
tests.append({'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0})
tests.append({'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3})
tests.append({'input': {'cards': [6], 'query': 6}, 'output': 0})
tests.append({'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1})
tests.append({'input': {'cards': [], 'query': 7}, 'output': -1})
tests.append({'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7})
tests.append({'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2})

if __name__ == '__main__':
    unittest.main()