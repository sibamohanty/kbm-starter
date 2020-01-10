""" Cornice services.
"""
from cornice import Service
from cornice.resource import resource
import json
from kbm.models import Kbm, DBSession


# @view_config(route_name='search', renderer='json')
# def KbmSearch(request):
#     pass

@resource(collection_path='/articles', path='/articles/{id}')
class KbmView(object):

    def __init__(self, request):
        self.request = request

    def collection_get(self):

        return {
            'articles': [
                {'id': kbm.id, 'title': kbm.title, 'description': kbm.description,
                'create_at': kbm.create_at, 'create_by': kbm.create_by, 'priority': kbm.priority}

                    for kbm in DBSession.query(Kbm)

                    ]
            }

    def get(self):
        try:
            kbm_id = int(self.request.matchdict['id'])
            return DBSession.query(Kbm).get(kbm_id).to_json()

        except:
            return {"error": "Something went wrong!"}

    def collection_post(self):
        try:
            kbm = self.request.json
            DBSession.add(Kbm.from_json(kbm))
            return DBSession.query(Kbm).order_by(Kbm.id.desc()).first().to_json()

        except:
            return {"error": "Something went wrong!"}

    def put(self):
        try:
            obj=DBSession.query(Kbm).filter(Kbm.id==self.request.matchdict['id'])
            # print(len(obj))
            obj.update(self.request.json)
            return {'articles': [
                    {'id': kbm.id, 'title': kbm.title, 'description': kbm.description,
                    'create_at': kbm.create_at, 'create_by': kbm.create_by, 'priority': kbm.priority}

                        for kbm in DBSession.query(Kbm)

                        ]
                    }
        except:
            return {'result': 'No object found'}

    def delete(self):
        obj=DBSession.query(Kbm).filter(Kbm.id==self.request.matchdict['id']).first()
        DBSession.delete(obj)

        return {'articles': [
                {'id': kbm.id, 'title': kbm.title, 'description': kbm.description,
                'create_at': kbm.create_at, 'create_by': kbm.create_by, 'priority': kbm.priority}

                    for kbm in DBSession.query(Kbm)

                    ]
                }
