from Calculator_AWC_query import External_calculator_zzz
import os 

#def generate_DFA():
    #depend on fastener_types to generate different DFA describe the 2 boards and the faster

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
    
    data = data.replace("<fast_dia>", str(ins_connection.ConnectionBlot.fast_dia))
    
    if ins_connection.ConnectionBlot.fast_dia == "0.25":
        PARAMS_type = "_1_4"
    elif ins_connection.ConnectionBlot.fast_dia == "0.3125":
        PARAMS_type = "_5_16"
    elif ins_connection.ConnectionBlot.fast_dia == "0.375":
        PARAMS_type = "_3_8"
    elif ins_connection.ConnectionBlot.fast_dia == "0.4375":
        PARAMS_type = "_7_16"
    elif ins_connection.ConnectionBlot.fast_dia == "0.5":
        PARAMS_type = "_1_2"
    elif ins_connection.ConnectionBlot.fast_dia == "0.625":
        PARAMS_type = "_5_8"
    elif ins_connection.ConnectionBlot.fast_dia == "0.75":
        PARAMS_type = "_3_4"
    elif ins_connection.ConnectionBlot.fast_dia == "0.875":
        PARAMS_type = "_7_8"
    elif ins_connection.ConnectionBlot.fast_dia == "1":
        PARAMS_type = "_1_1"
    else:
        print("bolt type error")
        pass
        
    data = data.replace("<bolt_type>", "bolt" + PARAMS_type + "_zzz")
    data = data.replace("<nut_type>", "nut" + PARAMS_type + "_zzz")

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

    if ins_connection.ConnectionNail.nail_size == "6d":
        PARAMS_nail_size = 0.099
        PARAMS_ls_length = 2
    elif ins_connection.ConnectionNail.nail_size == "7d":
        PARAMS_nail_size = 0.099
        PARAMS_ls_length = 2.25
    elif ins_connection.ConnectionNail.nail_size == "8d":
        PARAMS_nail_size = 0.113
        PARAMS_ls_length = 2.5
    elif ins_connection.ConnectionNail.nail_size == "10d":
        PARAMS_nail_size = 0.128
        PARAMS_ls_length = 3
    elif ins_connection.ConnectionNail.nail_size == "12d":
        PARAMS_nail_size = 0.128
        PARAMS_ls_length = 3.25
    elif ins_connection.ConnectionNail.nail_size == "16d":
        PARAMS_nail_size = 0.135
        PARAMS_ls_length = 3.5
    elif ins_connection.ConnectionNail.nail_size == "20d":
        PARAMS_nail_size = 0.148
        PARAMS_ls_length = 4
    elif ins_connection.ConnectionNail.nail_size == "30d":
        PARAMS_nail_size = 0.148
        PARAMS_ls_length = 4.5
    elif ins_connection.ConnectionNail.nail_size == "40d":
        PARAMS_nail_size = 0.162
        PARAMS_ls_length = 5
    else:
        print("nail type error")
        pass
        
    data = data.replace("<nail_size>", str(PARAMS_nail_size))
    data = data.replace("<ls_length_09>", str(PARAMS_ls_length * 0.9))
    data = data.replace("<ls_length_01>", str(PARAMS_ls_length * 0.1))

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()
    
def generate_lag_screw(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    print("data from template:", data)

    # data = data.replace("<PARAM1>", str(leg_length))
    # data = data.replace("<PARAM2>", str(leg_side))
    # data = data.replace("<PARAM3>", str(top_lenght))
    # data = data.replace("<PARAM4>", str(top_width))
    # data = data.replace("<PARAM5>", str(top_height))

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()
    
def generate_wood_screw(ins_connection, PATH_TO_DFA, DFA_FILE_NAME):
    # Read the content of the template file
    f = open(PATH_TO_DFA + "\\template\\" + DFA_FILE_NAME, "r")
    data = f.read()
    print("data from template:", data)

    # data = data.replace("<PARAM1>", str(leg_length))
    # data = data.replace("<PARAM2>", str(leg_side))
    # data = data.replace("<PARAM3>", str(top_lenght))
    # data = data.replace("<PARAM4>", str(top_width))
    # data = data.replace("<PARAM5>", str(top_height))

    f = open(PATH_TO_DFA + "\\" + DFA_FILE_NAME, "w")
    f.write(data)
    f.close()

if __name__ == "__main__":
    instance=External_calculator_zzz()

    
    instance.ConnectionBlot.fast_dia="0.5"          #inch *IMPORTANT*
    
    instance.ConnectionLagScrew.wash_thickness="0.125"  #inch *IMPORTANT*
    instance.ConnectionLagScrew.fast_dia="0.25"         #inch *IMPORTANT*
    instance.ConnectionLagScrew.ls_length="2.5"         #inch *IMPORTANT*
    
    instance.ConnectionWoodScrew.fast_dia="0.151"       #inch *IMPORTANT*
    instance.ConnectionWoodScrew.ls_length="2"          #inch *IMPORTANT*
    
    instance.ConnectionNail.fast_dia="sinker"       #common wire, sinker, box  *IMPORTANT*
    instance.ConnectionNail.nail_size="7d"          #6 7 8 10 12 16 20 30 40   *IMPORTANT*

    #the two boards
    instance.mm_type="Alaska+Cedar"      #zl: different types have different density. will not change in this example
    instance.mm_thickness="-1"           #"-1" means user-define value. will not change in this example
    instance.mm_thickness_text="1"       #inch  *IMPORTANT*
    instance.theta_angle_mm="0"          #angle between grain and load. will not change in this example
    instance.theta_angle_sm="0"          #angle between grain and load. will not change in this example
    instance.sm_type="Alaska+Cedar"      #inch
    instance.sm_thickness="-1"           #"-1" means user-define value. will not change in this example
    instance.sm_thickness_text="1"       #inch  *IMPORTANT*

#----------------------------------------------------
    instance.design_method="ASD"         #zl: allowable stress design. will not change in this example
    instance.connection_type="Lateral+loading"   #zl: withdrawal loading. will not change in this example
    
    #connection way
    instance.fastener_types="Bolt"       #Bolt, Lag+Screw, Wood+Screw, Nail  *IMPORTANT*
    instance.loading_scenario="Single+Shear" #"Single+Shear" for default. will not change in this example
    
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