import unittest

from pyramid import testing

class KbmModelTests(unittest.TestCase):
    def _getTargetClass(self):
        from .models import Kbm
        return Kbm
    def _makeOne(self, title="title", description="description",
                 create_at="at", create_by="Somename", priority=4):

        return self._getTargetClass()(title, description, create_at, create_by, priority)
    def test_constructor(self):
        instance =self._makeOne()
        self.assertEqual(instance.title, u'title')
        self.assertEqual(instance.description, u'description')
        self.assertEqual(instance.create_at, u'at')
        self.assertEqual(instance.create_by, u'Somename')
        self.assertEqual(instance.priority, 4)

    def test_constructor_wrong_param(self):
        instance = self._makeOne()
        self.assertNotEqual(instance.priority, 2)
