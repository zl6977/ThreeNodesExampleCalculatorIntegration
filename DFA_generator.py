from Calculator_AWC_query import External_calculator_zzz
import os 

def updateTemplate(ins_connection):
    # Read the content of the template file
    PATH_TO_DFA = os.path.abspath(os.path.join(os.getcwd(), "DFA_files\\"))
    DFA_FILE_NAME = "xx.dfa"
    if ins_connection.fastener_types == "Bolt":
        DFA_FILE_NAME = "twoboardtoconnect_bolt.dfa"
        generate_bolt(ins_connection,PATH_TO_DFA,DFA_FILE_NAME)
    elif ins_connection.fastener_types == "Lag+Screw":
        DFA_FILE_NAME = "twoboardtoconnect_lagScrew.dfa"
        generate_lag_screw(ins_connection,PATH_TO_DFA,DFA_FILE_NAME)
    elif ins_connection.fastener_types == "Wood+Screw":
        DFA_FILE_NAME = "twoboardtoconnect_woodScrew.dfa"
        generate_wood_screw(ins_connection,PATH_TO_DFA,DFA_FILE_NAME)
    elif ins_connection.fastener_types == "Nail":
        DFA_FILE_NAME = "twoboardtoconnect_nail.dfa"
        generate_nail(ins_connection,PATH_TO_DFA,DFA_FILE_NAME)
    else:
        print("fastener_types error")
        pass

def generate_bolt(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    # print("data from template:", data)

    data = data.replace("<mm_thickness_text>", str(ins_connection.mm_thickness_text))
    data = data.replace("<sm_thickness_text>", str(ins_connection.sm_thickness_text))
    data = data.replace("<connection_capacity>", str(ins_connection.connection_capacity))
    data = data.replace("<connection_requirement>", str(ins_connection.connection_requirement))
    
    data = data.replace("<mm_length>", str(ins_connection.mm_length))
    data = data.replace("<mm_width>", str(ins_connection.mm_width))
    data = data.replace("<sm_length>", str(ins_connection.sm_length))
    data = data.replace("<sm_width>", str(ins_connection.sm_width))
    
    shank_dia = ["0.25","0.3125","0.375","0.4375","0.5","0.625","0.75","0.875","1"]
    PARAMS_type = ["_1_4","_5_16","_3_8","_7_16","_1_2","_5_8","_3_4","_7_8","_1_1"]
    try:
        i = shank_dia.index(ins_connection.ConnectionBlot.fast_dia)
    except ValueError:
        print("bolt type error")
        return
    
    data = data.replace("<fast_dia>", str(ins_connection.ConnectionBlot.fast_dia))
    data = data.replace("<bolt_type>", "bolt" + PARAMS_type[i] + "_zzz")
    data = data.replace("<nut_type>", "nut" + PARAMS_type[i] + "_zzz")

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()
    
def generate_nail(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    # print("data from template:", data)

    data = data.replace("<mm_thickness_text>", str(ins_connection.mm_thickness_text))
    data = data.replace("<sm_thickness_text>", str(ins_connection.sm_thickness_text))
    data = data.replace("<connection_capacity>", str(ins_connection.connection_capacity))
    data = data.replace("<connection_requirement>", str(ins_connection.connection_requirement))

    data = data.replace("<mm_length>", str(ins_connection.mm_length))
    data = data.replace("<mm_width>", str(ins_connection.mm_width))
    data = data.replace("<sm_length>", str(ins_connection.sm_length))
    data = data.replace("<sm_width>", str(ins_connection.sm_width))

    nail_size_list = ["6d","7d","8d","10d","12d","16d","20d","30d","40d"]
    PARAMS_nail_size = [0.099,0.099,0.113,0.128,0.128,0.135,0.148,0.148,0.162]
    PARAMS_ls_length = [2,2.25,2.5,3,3.25,3.5,4,4.5,5]
    try:
        i = nail_size_list.index(ins_connection.ConnectionNail.nail_size)
    except ValueError:
        print("nail type error")
        return
    
    data = data.replace("<nail_size>", str(PARAMS_nail_size[i]))
    data = data.replace("<ls_length_09>", str(PARAMS_ls_length[i] * 0.9))
    data = data.replace("<ls_length_01>", str(PARAMS_ls_length[i] * 0.1))

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()
    
def generate_lag_screw(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    # print("data from template:", data)

    data = data.replace("<mm_thickness_text>", str(ins_connection.mm_thickness_text))
    data = data.replace("<sm_thickness_text>", str(ins_connection.sm_thickness_text))
    data = data.replace("<connection_capacity>", str(ins_connection.connection_capacity))
    data = data.replace("<connection_requirement>", str(ins_connection.connection_requirement))

    data = data.replace("<mm_length>", str(ins_connection.mm_length))
    data = data.replace("<mm_width>", str(ins_connection.mm_width))
    data = data.replace("<sm_length>", str(ins_connection.sm_length))
    data = data.replace("<sm_width>", str(ins_connection.sm_width))
    
    fast_dia_list = ["0.25","0.3125","0.375","0.4375","0.5","0.625","0.75","0.875","1"]
    PARAMS_outter_dia_washer = [0.489,0.586,0.683,0.779,0.873,0.971,1.079,1.176,1.271,1.367,1.464,1.560,1.661]
    try:
        i = fast_dia_list.index(ins_connection.ConnectionLagScrew.fast_dia)
    except ValueError:
        print("lag screw type error")
        return
    
    data = data.replace("<diameter_lag_screw>", str(ins_connection.ConnectionLagScrew.fast_dia))
    data = data.replace("<outter_dia_washer>", str(PARAMS_outter_dia_washer[i]))
    data = data.replace("<ls_length>", str(ins_connection.ConnectionLagScrew.ls_length))
    data = data.replace("<wash_thickness>", str(ins_connection.ConnectionLagScrew.wash_thickness))
    
    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()
    
def generate_wood_screw(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    # print("data from template:", data)

    data = data.replace("<mm_thickness_text>", str(ins_connection.mm_thickness_text))
    data = data.replace("<sm_thickness_text>", str(ins_connection.sm_thickness_text))
    data = data.replace("<connection_capacity>", str(ins_connection.connection_capacity))
    data = data.replace("<connection_requirement>", str(ins_connection.connection_requirement))

    data = data.replace("<mm_length>", str(ins_connection.mm_length))
    data = data.replace("<mm_width>", str(ins_connection.mm_width))
    data = data.replace("<sm_length>", str(ins_connection.sm_length))
    data = data.replace("<sm_width>", str(ins_connection.sm_width))
    
    data = data.replace("<diameter_wood_screw>", str(ins_connection.ConnectionWoodScrew.fast_dia))
    data = data.replace("<ls_length>", str(ins_connection.ConnectionWoodScrew.ls_length))

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()

if __name__ == "__main__":
    instance=External_calculator_zzz()

    #connection way
    instance.fastener_types="Lag+Screw"        #Bolt, Lag+Screw, Wood+Screw, Nail  *IMPORTANT*
    instance.loading_scenario="Single+Shear"    #"Single+Shear" for default. will not change in this example
    #parameters about fastner, only modify the related is enough
    instance.ConnectionBlot.fast_dia="0.5"          #inch *IMPORTANT*  0.25, 0.3125, 0.375, 0.4375, 0.5, 0.625, 0.75, 0.875, 1
    
    instance.ConnectionLagScrew.wash_thickness="0.125"  #inch *IMPORTANT*  0, 1/16, 2/16, 3/16, 4/16
    instance.ConnectionLagScrew.fast_dia="0.375"        #inch *IMPORTANT*  0.25, 0.3125, 0.375, 0.4375, 0.5, 0.625, 0.75, 0.875, 1
    instance.ConnectionLagScrew.ls_length="2.5"         #inch *IMPORTANT*  1,1.5,2,2.5,3,4,5,6,7,8,9,10,11,12
    
    instance.ConnectionWoodScrew.fast_dia="0.177"       #inch *IMPORTANT*  0.138,0.151,0.164,0.177,0.19,0.216,0.242,0.268,0.294,0.32,0.372 /6,7 8,9,10,12,14,16,18,20,24
    instance.ConnectionWoodScrew.ls_length="3"          #inch *IMPORTANT*  1,1.5,2,2.5,3,4,5,6,7,8,9,10,11,12
    
    instance.ConnectionNail.fast_dia="sinker"       #common wire, sinker, box  *IMPORTANT*
    instance.ConnectionNail.nail_size="6d"          #6 7 8 10 12 16 20 30 40   *IMPORTANT*

    #the two boards
    instance.mm_type="Alaska+Cedar"      #zl: different types have different density. will not change in this example
    instance.mm_thickness="-1"           #"-1" means user-define value. will not change in this example
    instance.mm_thickness_text="2.5"     #inch  *IMPORTANT* the downside one
    instance.theta_angle_mm="0"          #angle between grain and load. will not change in this example
    instance.theta_angle_sm="0"          #angle between grain and load. will not change in this example
    instance.sm_type="Alaska+Cedar"      #inch
    instance.sm_thickness="-1"           #"-1" means user-define value. will not change in this example
    instance.sm_thickness_text="0.6"       #inch  *IMPORTANT*
#-------rarely used------------------------------------
    instance.design_method="ASD"         #zl: allowable stress design. will not change in this example
    instance.connection_type="Lateral+loading"   #zl: withdrawal loading. will not change in this example
    #load condition
    instance.load_duration="1.0"         #will not change in this example
    instance.diaphragm="1.0"             #will not change in this example
    instance.end_grain="1.0"             #will not change in this example
    instance.wet_svc_factor="1.0"        #will not change in this example
    instance.temperature="1.0"           #will not change in this example
    instance.submit2_keywords="Calculate+Connection+Capacity"    #will not change in this example

    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.update_Adjusted_ASD_Capacity(),2), "kg")
    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.update_Adjusted_ASD_Capacity()/0.45359237,2), "lbs")
    updateTemplate(instance)