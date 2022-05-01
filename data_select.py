from connect import *

def select_im_s():
    try:
        tmp = "SELECT * FROM image_sensor;"
        im_s = execute_read_query(connection, tmp)
    except:
        im_s = "error"
    return im_s

def select_l_s():
    try:
        tmp = "SELECT * FROM level_sensor;"
        l_s = execute_read_query(connection, tmp)
    except:
        l_s = "error"
    return l_s

def select_p_s():
    try:
        tmp = "SELECT * FROM photo_sensor;"
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
        tmp = "SELECT * FROM object IN ORDER BY objectId DESC;"
        o = execute_read_query(connection, tmp)
    except:
        o = "error"
    return o