from random import randint
from unittest import TestCase
from uuid import uuid4

from extended_dataclass import dataclass, fromdict


class TestExtendedDataclass(TestCase):
    def test_from_dict(self):

        @dataclass
        class SampleDataclass(object):
            index: int = 0
            val: str = 'test'
            index2: int = 1

            def sample_func(self):
                pass

        sample_dict = {
            'index': randint(0, 10),
            'index2': randint(0, 10),
            'val': str(uuid4()),
            'val2': str(uuid4())
        }

        cls = fromdict(SampleDataclass, sample_dict)
        self.assertTrue(hasattr(cls, 'index'))
        self.assertTrue(hasattr(cls, 'index2'))
        self.assertTrue(hasattr(cls, 'val'))
        self.assertFalse(hasattr(cls, 'val2'))

        self.assertEqual(cls.index, sample_dict['index'])
        self.assertEqual(cls.index2, sample_dict['index2'])
        self.assertEqual(cls.val, sample_dict['val'])
