from connect import *

def select_im_s():
    try:
        tmp = "SELECT * FROM image_sensor ORDER BY imSNum DESC LIMIT 10;"
        im_s = execute_read_query(connection, tmp)
    except:
        im_s = "error"
    return im_s

def select_l_s():
    try:
        tmp = "SELECT * FROM level_sensor ORDER BY lSNum DESC LIMIT 10;"
        l_s = execute_read_query(connection, tmp)
    except:
        l_s = "error"
    return l_s

def select_p_s():
    try:
        tmp = "SELECT * FROM photo_sensor ORDER BY pSNum DESC LIMIT 10;"
        p_s = execute_read_query(connection, tmp)
    except:
        p_s = "error"
    return p_s

def select_model():
    try:
        tmp = "SELECT * FROM model;"
        m = execute_read_query(connection, tmp)
    except:
        m = "error"
    return m

def select_object():
    try:
        tmp = "SELECT * FROM object ORDER BY objectId DESC LIMIT 10;"
        o = execute_read_query(connection, tmp)
    except:
        o = "error"
    return o