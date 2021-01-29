from Calculator_AWC_query import External_calculator_zzz
import DFA_generator as DFA_gen

if __name__ == "__main__":
    instance=External_calculator_zzz()

    #connection way
    instance.fastener_types="Lag+Screw"        #Bolt, Lag+Screw, Wood+Screw, Nail  *IMPORTANT*
    instance.loading_scenario="Single+Shear"    #"Single+Shear" for default. will not change in this example
    instance.connection_requirement = "10"
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
    instance.sm_thickness_text="0.2"       #inch  *IMPORTANT*
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
    DFA_gen.updateTemplate(instance)
