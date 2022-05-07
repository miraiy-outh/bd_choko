from connect import *

def insert_im_s(im_id, total, good, bad):
    try:
        tmp = f"INSERT image_sensor (imageSensorId, total, good, bad, imSDate) VALUES ({im_id}, {total}, {good}, {bad}, CURTIME());"
        im_s = execute_query(connection, tmp)
    except:
        im_s = "error"
    return im_s

def insert_l_s(l_id, cr_lvl, is_cr, level):
    try:
        tmp = f"INSERT level_sensor (levelSensorId, criticalLevel, isCritical, level, lSDate) VALUES ({l_id}, {cr_lvl}, {is_cr}, {level}, CURTIME());"
        l_s = execute_query(connection, tmp)
    except:
        l_s = "error"
    return l_s

def insert_p_s(p_id, is_dec, lvl_ob):
    try:
        tmp = f"INSERT photo_sensor (photoSensorId, isDetectedObject, levelObject, pSDate) VALUES ({p_id}, {is_dec}, {lvl_ob}, CURTIME());"
        p_s = execute_query(connection, tmp)
    except:
        p_s = "error"
    return p_s

def insert_object(m_id, x, y, square):
    try:
        tmp = f"INSERT object (modelId, coordX, coordY, square, oDate) VALUES ({m_id}, {x}, {y}, {square}, CURTIME());"
        o = execute_query(connection, tmp)
    except:
        o = "error"
    return o