from unittest import TestCase

from extended_dataclass import DataClassPlus


class TestDataClassPlus(TestCase):
    def test_encode_basic(self):
        class TestClass(DataClassPlus):
            index: int = 0
            index2: int = 1
            val: str = "test"
            val2: str = None

        sample_dict = {
            "index": 3,
            "val": "test2"
        }

        encoded = TestClass().from_dict(sample_dict)
        # assert that what came out of the dict was set
        self.assertEqual(sample_dict["index"], encoded.index)
        self.assertEqual(sample_dict["val"], encoded.val)
        # assert defaults
        self.assertEqual(encoded.index2, 1)
        self.assertIsNone(encoded.val2)

    def test_encode_decode_with_subclass(self):
        class TestSubclass(DataClassPlus):
            index: int = 3

        class TestClass(DataClassPlus):
            index: int = 1
            val: str = "thisisavalue"
            sub: TestSubclass = None
            # lst: List[TestSubclass] = field(default_factory=list)

        sample_dict = {
            "index": 13,
            "val": "test",
            "sub": {"index": 4}
        }
        encoded = TestClass().from_dict(sample_dict)
        self.assertEqual(sample_dict["index"], encoded.index)
        self.assertEqual(sample_dict["val"], encoded.val)
        self.assertIsInstance(encoded.sub, DataClassPlus)
        self.assertIsInstance(encoded.sub, TestSubclass)
        self.assertEqual(sample_dict["sub"]["index"], encoded.sub.index)
        self.assertDictEqual(sample_dict, encoded.to_dict())
