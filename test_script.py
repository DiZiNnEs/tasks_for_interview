import unittest
import script


class MyTestCase(unittest.TestCase):
    result = {'D': {'deny': {'R': True}, 'address': {'R': '2gis.url.com'}, 'timeout': {'N': 1050, 'O': 50},
                    'verbose': {'A': True}, 'proxy-server': {'U': '3.102.198.51'}}}
    first_result_json = script.read_json_file('first_data.json')
    second_result_json = script.read_json_file('second_data.json')

    def test_something(self):
        self.assertEqual(script.get_different_between_two_files(self.first_result_json, self.second_result_json), self.result)


if __name__ == '__main__':
    unittest.main()
