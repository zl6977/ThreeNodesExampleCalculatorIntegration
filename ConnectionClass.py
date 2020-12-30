# import requests
# import bs4

#later, define and input a class containing the parameters of the 2 boards 
class ConnectionClass_zzz():
    design_method="ASD"
    connection_type="Lateral+loading"
    
    #the two boards
    mm_type="Alaska+Cedar"      #zl: different types decide different density
    mm_thickness="-1"           #"-1" means user-define value
    mm_thickness_text="11"
    theta_angle_mm="0"
    sm_type="Alaska+Cedar"
    sm_thickness="-1"           #"-1" means user-define value
    sm_thickness_text="10"
    
    #connection way
    fastener_types="Bolt"
    loading_scenario="Single+Shear" #"Single+Shear" for default
    
    fast_dia="0.5"
    load_duration="1.0"
    wet_svc_factor="1.0"
    temperature="1.0"
    submit2_LBS="Calculate+Connection+Capacity"
    

if __name__ == "__main__":
    instance=ConnectionClass_zzz()

    print("The Adjusted_ASD_Capacity of bolt connection is", instance.get_bolt_Adjusted_ASD_Capacity(), "kg")