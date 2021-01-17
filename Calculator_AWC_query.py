import requests
from ConnectionClass import ConnectionClass_zzz 
# import bs4

#later, define and input a class containing the parameters of the 2 boards 
class External_calculator_zzz(ConnectionClass_zzz):
    URL = "https://www.awc.org/calculators/connectioncalc.160106/ccstyle.asp?"
    def generate_para_bolt(self):
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
        PARAMS += "fast_dia="+ self.ConnectionBlot.fast_dia + "&"
        PARAMS += "load_duration="+ self.load_duration + "&"
        PARAMS += "wet_svc_factor="+ self.wet_svc_factor + "&"
        PARAMS += "temperature="+ self.temperature + "&"
        PARAMS += "submit2_LBS="+ self.submit2_keywords
        return PARAMS

    def generate_para_lagScrew(self):
        PARAMS = ""
        PARAMS += "design_method="+ self.design_method + "&"
        PARAMS += "connection_type="+ self.connection_type + "&"
        PARAMS += "fastener_types="+ self.fastener_types + "&"
        PARAMS += "loading_scenario="+ self.loading_scenario + "&"
        PARAMS += "mm_type="+ self.mm_type + "&"
        PARAMS += "mm_thickness="+ self.mm_thickness + "&"
        PARAMS += "mm_thickness_text="+ self.mm_thickness_text + "&"
        PARAMS += "theta_angle_mm="+ self.theta_angle_mm + "&"
        PARAMS += "wash_thickness="+ self.ConnectionLagScrew.wash_thickness + "&"
        PARAMS += "sm_type="+ self.sm_type + "&"
        PARAMS += "sm_thickness="+ self.sm_thickness + "&"
        PARAMS += "sm_thickness_text="+ self.sm_thickness_text + "&"
        PARAMS += "theta_angle_sm="+ self.theta_angle_sm + "&"
        PARAMS += "fast_dia="+ self.ConnectionLagScrew.fast_dia + "&"
        PARAMS += "ls_length="+ self.ConnectionLagScrew.ls_length + "&"
        PARAMS += "load_duration="+ self.load_duration + "&"
        PARAMS += "wet_svc_factor="+ self.wet_svc_factor + "&"
        PARAMS += "end_grain="+ self.end_grain + "&"
        PARAMS += "temperature="+ self.temperature + "&"
        PARAMS += "submit2_LLSS="+ self.submit2_keywords
        return PARAMS
        
    def generate_para_woodScrew(self):
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
        PARAMS += "fast_dia="+ self.ConnectionWoodScrew.fast_dia + "&"
        PARAMS += "ls_length="+ self.ConnectionWoodScrew.ls_length + "&"
        PARAMS += "load_duration="+ self.load_duration + "&"
        PARAMS += "wet_svc_factor="+ self.wet_svc_factor + "&"
        PARAMS += "end_grain="+ self.end_grain + "&"
        PARAMS += "temperature="+ self.temperature + "&"
        PARAMS += "submit2_LWSS="+ self.submit2_keywords
        return PARAMS

    def generate_para_nail(self):
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
        PARAMS += "nail_size="+ self.ConnectionNail.nail_size + "&"
        PARAMS += "fast_dia="+ self.ConnectionNail.fast_dia + "&"
        # PARAMS += "ls_length="+ self.ConnectionNail.ls_length + "&"
        PARAMS += "load_duration="+ self.load_duration + "&"
        PARAMS += "wet_svc_factor="+ self.wet_svc_factor + "&"
        PARAMS += "end_grain="+ self.end_grain + "&"
        PARAMS += "temperature="+ self.temperature + "&"
        PARAMS += "diaphragm="+ self.diaphragm + "&"
        PARAMS += "submit2_LNS="+ self.submit2_keywords      
        return PARAMS
        
    def update_Adjusted_ASD_Capacity(self):
        #1. generate params
        PARAMS = ""
        if self.fastener_types == "Bolt":
            PARAMS = self.generate_para_bolt()
        elif self.fastener_types == "Lag+Screw":
            PARAMS = self.generate_para_lagScrew()
        elif self.fastener_types == "Wood+Screw":
            PARAMS = self.generate_para_woodScrew()
        elif self.fastener_types == "Nail":
            PARAMS = self.generate_para_nail()
        else:
            print("fastener_types error")
            pass
        
        # sending get request and saving the response as response object
        r = requests.get(url = self.URL, params = PARAMS)         
        #Checking the result
        # print("Result:", r.text)
        # Parse the string r.text
        index_tmp = r.text.rfind("lbs.") #the last "lbs." as keyword to find the "Adjusted ASD Capacity"
        string_result = r.text[index_tmp-5 : index_tmp]
        string_tmp = ""
        # to extract the number from the string
        for charactor in string_result:
            if charactor >="0" and charactor <="9":
                string_tmp += charactor
        try:
            number_result_lbs = float(string_tmp)
            number_result = number_result_lbs * 0.45359237  #1 lbs = 0.45359237 kg
            self.connection_capacity = string_tmp   #update the value in class
            return number_result
        except ValueError:
            print("Query ERROR: result is:", r.text[index_tmp-500 : index_tmp+50])

if __name__ == "__main__":
    instance=External_calculator_zzz()
    instance.fastener_types="Nail"          #Bolt, Lag+Screw, Wood+Screw, Nail  *IMPORTANT*

    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.update_Adjusted_ASD_Capacity(),2), "kg")
    print("The Adjusted_ASD_Capacity of", str(instance.fastener_types), ":", round(instance.update_Adjusted_ASD_Capacity()/0.45359237,2), "lbs")
