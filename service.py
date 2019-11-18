from models import ToDoModel
from modelResults import prediction,prediction_contact
from trainModel import createmodel_Contact,createmodel_Wholesale
class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        return self.model.create(params)

    def update(self, item_id, params):
        return self.model.update(item_id, params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def list(self):
        response = self.model.list_items()
        return response

def model(params):
    print(params)
    return prediction(params)

def modelContact(params):
    print(params)
    return prediction_contact(params)

def trainModelContact():
    try:
        createmodel_Contact()
        return 0
    except:
        return -1

def trainModelWH():
    try:
        createmodel_Wholesale()
        return 0
    except:
        return -1
