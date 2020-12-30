# import requests
# import bs4

#this is a partial-capacity verision of the origianl calculator, so only parts of the variables are considered
#define and input a class containing the parameters of the 2 boards
class ConnectionClass_zzz():
    design_method="ASD"         #zl: allowable stress design. will not change in this example
    connection_type="Lateral+loading"   #zl: withdrawal loading. will not change in this example
    
    #the two boards
    mm_type="Alaska+Cedar"      #zl: different types decide different density. will not change in this example
    mm_thickness="-1"           #"-1" means user-define value. will not change in this example
    mm_thickness_text="11"      #inch
    theta_angle_mm="0"          #angle between grain and load. will not change in this example
    sm_type="Alaska+Cedar"      #inch
    sm_thickness="-1"           #"-1" means user-define value. will not change in this example
    sm_thickness_text="10"      #inch
    
    #connection way
    fastener_types="Bolt"       #Bolt, Lag+Screw, Wood+Screw, Nail
    loading_scenario="Single+Shear" #"Single+Shear" for default. will not change in this example
    
    #load condition
    load_duration="1.0"         #will not change in this example
    end_grain="1.0"             #will not change in this example
    wet_svc_factor="1.0"        #will not change in this example
    temperature="1.0"           #will not change in this example
    submit2_keywords="Calculate+Connection+Capacity"    #will not change in this example
    class ConnectionBlot():    
        fast_dia="0.5"          #inch    class ConnectionLagScrew():    
        wash_thickness="0.125"  #inch
        fast_dia="0.25"         #inch
        ls_length="2.5"         #inch
    class ConnectionWoodScrew():    
        fast_dia="0.138"        #inch
        ls_length="2.5"         #inch
    class ConnectionNail():    
        fast_dia="box"  #common wire, sinker, box
        nail_size="6d"  #6 7 8 10 12 16 20 30 40