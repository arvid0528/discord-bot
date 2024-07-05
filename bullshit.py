import json
from json.decoder import JSONDecodeError
import os
import pathlib

def increase_bullshit_meter(user):

    data = {"user":[]}

    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "bullshitmeters.json"), "r") as fr:
        try:
            data = json.load(fr)
        except JSONDecodeError:
            pass       

        meter_level = -1
        for meters in data.values():
            for meter in meters:
                user_id = list(meter)[0]
                if user_id == str(user):
                    meter[user_id] += 1
                    meter_level = meter[user_id]

    if meter_level == -1:
        data["user"].append({str(user):1})

    with open(os.path.join(pathlib.Path(__file__).parent.resolve(), "bullshitmeters.json"), "w") as fw:
        json.dump(data, fw)

    if meter_level%10 == 0:
        return True
    return False