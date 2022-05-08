from connect import *

def persent_success_ims(num):
    total = execute_read_query(connection, f"SELECT total FROM image_sensor WHERE imageSensorId = {num} ORDER BY imSNum DESC LIMIT 1;")[0][0]
    good = execute_read_query(connection, f"SELECT good FROM image_sensor WHERE imageSensorId = {num} ORDER BY imSNum DESC LIMIT 1;")[0][0]
    perc = (good / total) * 100

    return perc

def level_ls(num):
    lvl = execute_read_query(connection, f"SELECT level FROM level_sensor WHERE levelSensorId = {num} ORDER BY lSNum DESC LIMIT 1;")[0][0]

    return lvl
