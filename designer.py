from calculator_AWC_query import External_calculator_zzz

if __name__ == "__main__":
    instance=External_calculator_zzz()
    instance.fastener_types="Nail"          #Bolt, Lag+Screw, Wood+Screw, Nail  *IMPORTANT*
    
    instance.ConnectionBlot.fast_dia="0.5"          #inch *IMPORTANT*
    
    instance.ConnectionLagScrew.wash_thickness="0.125"  #inch *IMPORTANT*
    instance.ConnectionLagScrew.fast_dia="0.25"         #inch *IMPORTANT*
    instance.ConnectionLagScrew.ls_length="2.5"         #inch *IMPORTANT*
    
    instance.ConnectionWoodScrew.fast_dia="0.151"        #inch *IMPORTANT*
    instance.ConnectionWoodScrew.ls_length="2"           #inch *IMPORTANT*
    
    instance.ConnectionNail.ls_length="2"           #inch *IMPORTANT*
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


    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.get_Adjusted_ASD_Capacity(),2), "kg")
    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.get_Adjusted_ASD_Capacity()/0.45359237,2), "lbs")