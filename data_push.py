from connect import *

def insert_im_s(im_id, total, good, bad):
    try:
        tmp = f"UPDATE image_sensor SET total = {total}, good = {good}, bad = {bad} WHERE imageSensorId = {im_id};"
        im_s = execute_read_query(connection, tmp)
    except:
        im_s = "error"
    return im_s

def insert_l_s(l_id, cr_lvl, is_cr, level):
    try:
        tmp = f"UPDATE level_sensor SET criticalLevel = {cr_lvl}, isCritical = {is_cr}, level = {level} WHERE levelSensorId = {l_id};"
        l_s = execute_read_query(connection, tmp)
    except:
        l_s = "error"
    return l_s

def insert_p_s(p_id, is_dec, lvl_ob):
    try:
        tmp = f"UPDATE photo_sensor SET isDetectedObject = {is_dec}, levelObject = {lvl_ob} WHERE photoSensorId = {p_id};"
        p_s = execute_read_query(connection, tmp)
    except:
        p_s = "error"
    return p_s

def insert_object(m_id, x, y, square):
    try:
        tmp = f"INSERT object (modelId, coordX, coordY, square) VALUES ({m_id}, {x}, {y}, {square});"
        o = execute_read_query(connection, tmp)
    except:
        o = "error"
    return o