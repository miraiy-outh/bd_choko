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

    if tmp2 == 0:
        good2 += 1
    else:
        bad2 += 1

    if tmp3 == 0:
        good3 += 1
    else:
        bad3 += 1

    insert_im_s(1, total1 + 1, good1, bad1)
    insert_im_s(2, total2 + 1, good2, bad2)
    insert_im_s(3, total3 + 1, good3, bad3)

    return select_im_s()

def l_s_iter():
    return 0

while (True):
    print(im_s_iter())
    sleep(1)