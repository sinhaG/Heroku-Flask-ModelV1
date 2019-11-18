import pickle
import pandas as pd
filename = 'finalized_model.sav'
# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))

path = './data/clustering.csv'
data = pd.read_csv(path)

print(loaded_model.predict(data.iloc[[15]]))

def prediction(param):
    filename_func = 'finalized_model.sav'
    # load the model from disk
    loaded_model_func = pickle.load(open(filename_func, 'rb'))

    if param is None:
        return " No Results Param is empty" + param
    print(param)
    j = param
    print(j)
    df = pd.DataFrame.from_dict(j)

    #df = pd.read_json(param)
    print("in prediction================")
    print(df)
    result =  loaded_model_func.predict(df)
    print(result)
    return  str(result);

def prediction_contact(param):
    filename_func = 'contact_model.sav'
    loaded_model_func = pickle.load(open(filename_func, 'rb'))

    if param is None:
        return " No Results Param is empty" + param
    print(param)
    j = param
    print(j)
    df = pd.DataFrame.from_dict(j)

    #df = pd.read_json(param)
    print("in prediction================")
    print(df)
    result =  loaded_model_func.predict(df)
    print(result)
    return  str(result);

