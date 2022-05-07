from connect import *
from data_select import *
from data_push import *
from random import *
from time import *

def im_s_iter():
    total1 = execute_read_query(connection, "SELECT total FROM image_sensor WHERE imageSensorId = 1;")[0][0]
    total2 = execute_read_query(connection, "SELECT total FROM image_sensor WHERE imageSensorId = 2;")[0][0]
    total3 = execute_read_query(connection, "SELECT total FROM image_sensor WHERE imageSensorId = 3;")[0][0]

    good1 = execute_read_query(connection, "SELECT good FROM image_sensor WHERE imageSensorId = 1;")[0][0]
    good2 = execute_read_query(connection, "SELECT good FROM image_sensor WHERE imageSensorId = 2;")[0][0]
    good3 = execute_read_query(connection, "SELECT good FROM image_sensor WHERE imageSensorId = 3;")[0][0]

    bad1 = execute_read_query(connection, "SELECT bad FROM image_sensor WHERE imageSensorId = 1;")[0][0]
    bad2 = execute_read_query(connection, "SELECT bad FROM image_sensor WHERE imageSensorId = 2;")[0][0]
    bad3 = execute_read_query(connection, "SELECT bad FROM image_sensor WHERE imageSensorId = 3;")[0][0]

    tmp1 = randint(0, 1)
    tmp2 = randint(0, 1)
    tmp3 = randint(0, 1)

    if tmp1 == 0:
        good1 += 1
    else:
        bad1 += 1
    obj_iter(tmp1, 1)
    if tmp2 == 0:
        good2 += 1
    else:
        bad2 += 1
    obj_iter(tmp2, 2)
    if tmp3 == 0:
        good3 += 1
    else:
        bad3 += 1
    obj_iter(tmp3, 3)

    insert_im_s(1, total1 + 1, good1, bad1)
    insert_im_s(2, total2 + 1, good2, bad2)
    insert_im_s(3, total3 + 1, good3, bad3)

    return select_im_s()

def obj_iter(tmp, num):
    m_id = randint(1, 4)
    mdl_x = execute_read_query(connection, f"SELECT coordXModel FROM model WHERE modelId = {m_id};")[0][0]
    mdl_y = execute_read_query(connection, f"SELECT coordYModel FROM model WHERE modelId = {m_id};")[0][0]
    if tmp == 0:
        x = randint(1, mdl_x - 1)
        y = randint(1, mdl_x - 1)
    else:
        x = mdl_x
        y = mdl_y

    square = x * y
    insert_object(m_id, x, y, square)

def l_s_iter():
    is_cr1 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 1;")[0][0]
    is_cr2 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 2;")[0][0]
    is_cr3 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 3;")[0][0]

    massive = [0] * 3
    if is_cr1 != 1:
        massive[0] = 1
    if is_cr2 != 1:
        massive[1] = 1
    if is_cr3 != 1:
        massive[2] = 1
    tmp = randint(0, 2)
    while massive[tmp] != 1:
        tmp = randint(0, 2)
    cr_l = execute_read_query(connection, f"SELECT criticalLevel FROM level_sensor WHERE levelSensorId = {tmp + 1};")[0][0]
    lvl = execute_read_query(connection, f"SELECT level FROM level_sensor WHERE levelSensorId = {tmp + 1};")[0][0]
    lvl = lvl - 10
    insert_l_s(tmp + 1, cr_l, 0, lvl)
    if lvl <= cr_l:
        insert_l_s(tmp + 1, cr_l, 1, lvl)

    return select_l_s()

def l_s_cr():
    is_cr1 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 1;")[0][0]
    is_cr2 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 2;")[0][0]
    is_cr3 = execute_read_query(connection, "SELECT isCritical FROM level_sensor WHERE levelSensorId = 3;")[0][0]

    if is_cr1 == 1:
        lvl = execute_read_query(connection, "SELECT level FROM level_sensor WHERE levelSensorId = 1;")[0][0]
        cr_l = execute_read_query(connection, f"SELECT criticalLevel FROM level_sensor WHERE levelSensorId = 1;")[0][0]
        insert_l_s(1, cr_l, 0, lvl + 30)
    if is_cr2 == 1:
        lvl = execute_read_query(connection, "SELECT level FROM level_sensor WHERE levelSensorId = 2;")[0][0]
        cr_l = execute_read_query(connection, f"SELECT criticalLevel FROM level_sensor WHERE levelSensorId = 2;")[0][0]
        insert_l_s(2, cr_l, 0, lvl + 30)
    if is_cr3 == 1:
        lvl = execute_read_query(connection, "SELECT level FROM level_sensor WHERE levelSensorId = 3;")[0][0]
        cr_l = execute_read_query(connection, f"SELECT criticalLevel FROM level_sensor WHERE levelSensorId = 3;")[0][0]
        insert_l_s(3, cr_l, 0, lvl + 30)

def p_s_iter():
    is_det1 = randint(0, 1)
    is_det2 = randint(0, 1)
    is_det3 = randint(0, 1)

    if is_det1 == 1:
        lvl1 = randint(1, 100)
    else:
        lvl1 = 0
    if is_det2 == 1:
        lvl2 = randint(1, 100)
    else:
        lvl2 = 0
    if is_det3 == 1:
        lvl3 = randint(1, 100)
    else:
        lvl3 = 0

    insert_p_s(1, is_det1, lvl1)
    insert_p_s(2, is_det2, lvl2)
    insert_p_s(3, is_det3, lvl3)

    return select_p_s()

while (True):
    print("Показания датчиков изображения форм (id датчика, всего, хорошо, плохо):")
    print(im_s_iter())
    print("Показания датчиков уровня сырья в баков (id датчика, критический уровень, критический уровень?, текущий уроыень):")
    print(l_s_iter())
    print("Показания фотоэлектрических датчиков детектирования (id датчика, объект задетектирован?, уровень заполненности формы):")
    print(p_s_iter())
    print("Последние 5 объектов(id объекта, id модели, x, y, площадь):")
    print(select_object())
    print()
    sleep(1)
    l_s_cr()