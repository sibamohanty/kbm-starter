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

import requests, json

class KbmViewTests(unittest.TestCase):


    def setUp(self) :
        self.kbm_id = 0
        self.port = '6542'
        self.url = 'http://127.0.0.1:' + self.port + '/articles'
        self.headers = {'content-type': 'application/json'}
        testdata = {"title": "test data",
                    "create_at": "2017-08-23 00:00",
                    "create_by": "test 1",
                    "description": "test data description",
                    "priority": "3"
                }
        try:
            r = requests.post(self.url, data=json.dumps(testdata), headers=self.headers)
            assert r.status_code, 200
            result = json.loads(r.text)
            self.kbm_id = result['id']
        except:
            print("Something went wrong")

    def tearDown(self):
        r = requests.delete(self.url+ '/' +str(self.kbm_id))
        assert r.status_code,200

    def test_add_kbm(self):
        "setup has added a kbm, check if it exists"
        r = requests.get(self.url + '/' + str(self.kbm_id))
        # print(r.json())
        self.assertEqual(r.status_code,200)
        result = json.loads(r.text)
        # print(result)
        self.assertEqual(self.kbm_id, result['id'])
        # self.tearDown()

    def test_put_kbm(self):
        testdata = {"title": "test data 2",
                    "create_at": "2017-08-23 00:00",
                    "create_by": "test 4",
                    "description": "test data description",
                    "priority": "3"
                    }
        r = requests.put(self.url + '/' + str(self.kbm_id), data=json.dumps(testdata), headers=self.headers)
        # print(r.status_code)
        self.assertEqual(r.status_code, 200)
        r = requests.get(self.url + '/' + str(self.kbm_id))
        print(r.json())
        self.assertEqual(r.status_code, 200)
        result = json.loads(r.text)
        # print(result)
        self.assertEqual(self.kbm_id, result['id'])
        self.assertEqual(result["title"], testdata["title"])

    def test_delete_kbm(self):
        r = requests.delete(self.url + '/' + str(self.kbm_id))
        self.assertEqual(r.status_code,200)
