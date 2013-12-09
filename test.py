import unittest
from datetime import datetime
import pytz
import dson


class DSONTest(unittest.TestCase):
    
    def test_all(self):
        value = {
            'string': 'I\'m a string',
            'unicode': u'h\xf6d\xf6',
            'float': 23.32,
            'int': 123,
            'realy_big_int': 1000000000000000000,
            'bool': True,
            'bool_false': False,
            'none': None,
            'datetime': datetime.utcnow().replace(tzinfo=pytz.utc),
            'list': [1,2,3,"poodles",{'foo':'bar'},["poodles",4,5,6]]
        }
        bytes = dson.dumps(value)
        deserialized_value = dson.loads(bytes)
        self.assertEquals(deserialized_value, value)