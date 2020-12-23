import requests
# import bs4

#later, define and input a class containing the parameters of the 2 boards 
class External_calculator_zzz():
    design_method="ASD" # Allowable stress design
    connection_type="Lateral+loading"   # Withdrawal loading / 
    fastener_types="Wood+Screw"
    loading_scenario="Single+Shear"
    mm_type="Alaska+Cedar"
    mm_thickness="-1"
    mm_thickness_text="1"
    theta_angle_mm="0"
    sm_type="Alaska+Cedar"
    sm_thickness="-1"
    sm_thickness_text="1"
    fast_dia="0.151"
    ls_length="2.5"
    load_duration="1.0"
    wet_svc_factor="1.0"
    temperature="1.0"
    submit2_LBS="Calculate+Connection+Capacity"

# design_method=ASD
# &connection_type=Lateral+loading
# &fastener_types=Wood+Screw
# &loading_scenario=Single+Shear
# &mm_type=Alaska+Cedar
# &mm_thickness=2.5
# &mm_thickness_text=
# &theta_angle_mm=0
# &sm_type=Alaska+Cedar
# &sm_thickness=0.375
# &sm_thickness_text=
# &fast_dia=0.138
# &ls_length=2.5
# &load_duration=1.0
# &wet_svc_factor=1.0
# &end_grain=1.0&temperature=1.0&submit2_LWSS=Calculate+Connection+Capacity

    URL = "https://www.awc.org/calculators/connectioncalc.160106/ccstyle.asp?"
    # defining a query params
    # PARAMS = "design_method=ASD&connection_type=Lateral+loading&fastener_types=Bolt&loading_scenario=Single+Shear&mm_type=Glulam+AC&mm_thickness=2.5&mm_thickness_text=&theta_angle_mm=0&sm_type=Steel&sm_thickness=0.25&sm_thickness_text=&fast_dia=0.5&load_duration=1.0&wet_svc_factor=1.0&temperature=1.0&submit2_LBS=Calculate+Connection+Capacity"

    def get_bolt_Adjusted_ASD_Capacity(self):
        PARAMS = ""
        PARAMS += "design_method="+ self.design_method + "&"
        PARAMS += "connection_type="+ self.connection_type + "&"
        PARAMS += "fastener_types="+ self.fastener_types + "&"
        PARAMS += "loading_scenario="+ self.loading_scenario + "&"
        PARAMS += "mm_type="+ self.mm_type + "&"
        PARAMS += "mm_thickness="+ self.mm_thickness + "&"
        PARAMS += "mm_thickness_text="+ self.mm_thickness_text + "&"
        PARAMS += "theta_angle_mm="+ self.theta_angle_mm + "&"
        PARAMS += "sm_type="+ self.sm_type + "&"
        PARAMS += "sm_thickness="+ self.sm_thickness + "&"
        PARAMS += "sm_thickness_text="+ self.sm_thickness_text + "&"
        PARAMS += "fast_dia="+ self.fast_dia + "&"
        PARAMS += "ls_length="+ self.ls_length + "&"
        PARAMS += "load_duration="+ self.load_duration + "&"
        PARAMS += "wet_svc_factor="+ self.wet_svc_factor + "&"
        PARAMS += "temperature="+ self.temperature + "&"
        PARAMS += "submit2_LBS="+ self.submit2_LBS
         
        # sending get request and saving the response as response object
        r = requests.get(url = self.URL, params = PARAMS)
         
        #Checking the result
        # print("Result:", r.text)
         
        # Parse the string r.text        
        index_tmp = r.text.rfind("lbs.") #the last "lbs." as keyword to find the "Adjusted ASD Capacity"
        string_result = r.text[index_tmp-5 : index_tmp]
        print(r.text)
        number_result_lbs = float(string_result)
        number_result = number_result_lbs * 0.45359237  #1 lbs = 0.45359237 kg
        # print(float(number_result))
        return number_result

if __name__ == "__main__":
    instance=External_calculator_zzz()

    print("The Adjusted_ASD_Capacity of connection is", instance.get_bolt_Adjusted_ASD_Capacity(), "kg")
    print("The Adjusted_ASD_Capacity of connection is", instance.get_bolt_Adjusted_ASD_Capacity()/0.45359, "lbs")