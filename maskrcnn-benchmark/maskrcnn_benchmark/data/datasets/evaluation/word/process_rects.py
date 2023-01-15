import numpy as np

def is_good(quad): # Checks if a quad is approximately horizontal rectangle
    res = False
    x=sorted(quad[0::2])
    y=sorted(quad[1::2])
    if (abs(y[0]-y[1])+abs(y[2]-y[3]) <= 5) and (abs(x[0]-x[1])+abs(x[3]-x[2])) <= 5:
        res = True
        
    return res

def merge_rectangles(boxes,threshold):
    temp_final_boxes = []
    bool_arr = [False for i in range(len(boxes))]
    for i,box_1 in enumerate(boxes):
        for j,box_2 in enumerate(boxes):
            # Merge only if approximately horizontal rectangular boxes
            if (not np.array_equal(box_1, box_2)):
                if is_good(box_1):
                    if is_good(box_2):
                        if bool_arr[i]==False or bool_arr[j]==False:
                            box1 = [min(box_1[0::2]),min(box_1[1::2]),max(box_1[0::2]),max(box_1[1::2])]
                            box2 = [min(box_2[0::2]),min(box_2[1::2]),max(box_2[0::2]),max(box_2[1::2])]
                            if abs(box1[1]-box2[1]) + abs(box1[3]-box2[3]) < threshold:
                                #if ( abs(box1[2]-box2[0]) + (abs(box1[4]-box2[6])) <30 ) or ( abs(box1[0]-box2[2]) + abs(box1[6]-box2[4]) < 30 ) or (box1[0]<=box2[0]<=box1[2] and box1[6]<=box2[6]<=box1[4]) or (box1[0]<=box2[2]<=box1[2] and box1[6]<=box2[4]<=box1[4]):
                                if abs(box1[2]-box2[0])<10 or abs(box1[0]-box2[2])<10 or (box1[0]<=box2[0]<=box1[2]) or (box1[0]<=box2[2]<=box1[2]):
                                    new_min_x = min(box1[0],box2[0],box1[2],box2[2])
                                    new_min_y = min(box1[1],box2[1],box1[3],box2[3])
                                    new_max_x = max(box1[0],box2[0],box1[2],box2[2])
                                    new_max_y = max(box1[1],box2[1],box1[3],box2[3])
                                    new_box = [new_min_x,new_min_y,new_max_x,new_max_y]
                                    bool_arr[i] = True
                                    bool_arr[j] = True
                                    in_final_box = False
                                    for k in range(len(temp_final_boxes)):
                                        box_prev = temp_final_boxes[k]
                                        if abs(box_prev[1]-new_box[1]) + abs(box_prev[3]-new_box[3]) < threshold:
                                            if abs(box_prev[2]-new_box[0])<10 or abs(box_prev[0]-new_box[2])<10 or (box_prev[0]<=new_box[0]<=box_prev[2]) or (box_prev[0]<=new_box[2]<=box_prev[2]):
                                                newest_box = [min(box_prev[0],new_box[0]),min(box_prev[1],new_box[1]),max(box_prev[2],new_box[2]), max(box_prev[3],new_box[3])]
                                                temp_final_boxes[k] = newest_box
                                                in_final_box= True
                                    if in_final_box == False:
                                        #print("Nice")
                                        temp_final_boxes.append(new_box)

    final_boxes = []
    for each_box in temp_final_boxes:
        each_box_new = [each_box[0],each_box[1],each_box[2],each_box[1],each_box[2],each_box[3],each_box[0],each_box[3]]
        final_boxes.append(each_box_new)

    for i in range(len(boxes)):
        if bool_arr[i]==False and (boxes[i] not in temp_final_boxes):
            final_boxes.append(boxes[i])
    return np.array(final_boxes)