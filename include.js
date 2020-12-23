//Author: Cameron Knudson 2005
//-----------------------------------------------------------------
		//This function determines if the browser that hits this page is compatible with
		//some of the functionality that we have built into the calculator.
		//If it is not, it will redirect them to an "incompatible browser" page
		//-----------------------------------------------------------------
		function checkBrowser()
		{
			var passedBrowserCheck = 0;
			
			if (navigator.appName == "Netscape" && parseFloat(navigator.appVersion) >= 6.1)
			{
				//using Netscape 6.1+
				passedBrowserCheck = 1
				//alert("Browser: " + navigator.appName + '\n' + "Version: " + navigator.appVersion + '\n' + "UserAgent String: " + navigator.userAgent + '\n' + "Status: passed");
			}


			var version=0
			if (navigator.appVersion.indexOf("MSIE")!=-1)
			{
				var temp = navigator.appVersion.split("MSIE");
				version = parseFloat(temp[1]);
				if (version >= 5.0) //NON IE browser will return 0
				{
					//using IE 5.0+
					passedBrowserCheck = 1;
				}
				//alert("Browser: " + navigator.appName + '\n' + "Version: " + version + '\n' + "UserAgent String: " + navigator.userAgent + '\n' + "Status: passed");
			}

			if ((navigator.userAgent.indexOf("Opera 6")!=-1)||(navigator.userAgent.indexOf("Opera/6")!=-1))
			{
				//using Opera 6.0+
				passedBrowserCheck = 1;
				//alert("Browser: " + navigator.appName + '\n' + "Version: " + navigator.appVersion + '\n' + "UserAgent String: " + navigator.userAgent + '\n' + "Status: passed");
			}
			
			if(passedBrowserCheck == 0)
			{
				window.location.href='error.html';
				//alert("Browser: " + navigator.appName + '\n' + "Version: " + navigator.appVersion + '\n' + "UserAgent String: " + navigator.userAgent + '\n' + "Status: passed");
			}

			
		}
	function resetDropDown(objectToReset, valueToSetTo)
	{
	//alert("calling resetDropDown: " + objectToReset.name + "," + valueToSetTo);
		if( objectToReset != null) {
			var found = 0;
			for(i=0;i<objectToReset.options.length;i++) {
				if(objectToReset.options[i].value == valueToSetTo) {
					objectToReset.selectedIndex = i;
					found = 1;
					break;
				}
			}
			if(found == 0) {
				objectToReset.selectedIndex = 0;
			}
		}
	}

		//--------------------------------------------------------------------------------------
		//setFields(): This function gets all of the submitted values from the QueryString (url)
		//and populates any fields of this page's form (named form1) that have a matching name. 
		//i.e. if there is a length field in the form and the user submits the form back to 
		//this page then setFields() sets the value of the length form field to whatever the user 
		//submitted.
		//
		//This function is used in the body onload event to synchronize the form 
		//data with the new page's form when the user submits the page so they know what they
		//submitted.
		//
		//--------------------------------------------------------------------------------------
		function setFields() {
			var myurl = document.URL;
			vars = myurl.split("?");
			if(vars[1] != null) {
				//vars = vars[1];
				properties = vars[1].split("&");
				for(i=0;i<properties.length-1;i++) {
					myvar = properties[i].split("=");
					if(eval("document.form1." + myvar[0]) != null) {
						if(myvar[1] != "") {
							if(myvar[0] == "theta_angle_mm") {
								if(!isNaN(Number(myvar[1]))) {
									document.form1.theta_angle_mm.value = myvar[1];
								}
							}
							else if(myvar[0] == "theta_angle_sm") {
								if(!isNaN(Number(myvar[1]))) {
									document.form1.theta_angle_sm.value = myvar[1];
								}
							}
							else if(myvar[0] == "sm_thickness_text") {
								if(!isNaN(Number(myvar[1]))) {
									document.form1.sm_thickness_text.value = myvar[1];
								}
							}
							else if(myvar[0] == "mm_thickness_text") {
								if(!isNaN(Number(myvar[1]))) {
									document.form1.mm_thickness_text.value = myvar[1];
								}
							}
							else {
								setIndex = eval("document.form1." + myvar[0] + ".length");
								myvar[1] = unescape(myvar[1]);
								someVar = myvar[1].split("+");
								myvar[1] = someVar[0];
								for(k=1;k<someVar.length;k++)
									myvar[1] = myvar[1] + " " + someVar[k];
								for(j=0;j<setIndex;j++) {
										if(myvar[1] == eval("document.form1." + myvar[0] + "[" + j + "].value")) {
											//if (myvar[0] == "theta_angle_sm")
											//	alert("FOUND IT!\nmyvar[1]: " + myvar[1] + "\nvalue: " + eval("document.form1." + myvar[0] + "[" + j + "].value"));
											eval("document.form1." + myvar[0] + ".selectedIndex = " + j);
											break;
										}
								}
							}
						}
					}//end if the select is not null
				}
			}
		}
		
		//--------------------------------------------------------------------------------------
		//connection(): This function sets all of the options for the fasterner types and
		//loading scenario based on what the user selects for the connection type
		//--------------------------------------------------------------------------------------		
		function connection() {
			var connection = document.form1.connection_type;
			var fastener = document.form1.fastener_types;
			var scenario = document.form1.loading_scenario;
			var opt2, opt3;
				
			if (fastener != null && connection != null && scenario != null){	
				// delete all options for fastener and scenario
				fastener.length = 0
			
				tempscen = scenario.value;
				scenario.length = 0
				if (connection.value == "Withdrawal loading") {
					opt2 = new Option('Lag Screw', 'Lag Screw');
					fastener.options[fastener.options.length] = opt2;
					opt2 = new Option('Wood Screw', 'Wood Screw');
					fastener.options[fastener.options.length] = opt2;
					opt2 = new Option('Nail', 'Nail');
					fastener.options[fastener.options.length] = opt2;
					opt3 = new Option('N/A', 'N/A');
					scenario.options[scenario.options.length] = opt3;
				}
				else if (connection.value == "Lateral loading") {
					opt2 = new Option('Bolt', 'Bolt');
					fastener.options[fastener.options.length] = opt2;
					opt2 = new Option('Lag Screw', 'Lag Screw');
					fastener.options[fastener.options.length] = opt2;
					opt2 = new Option('Wood Screw', 'Wood Screw');
					fastener.options[fastener.options.length] = opt2;
					opt2 = new Option('Nail', 'Nail');
					fastener.options[fastener.options.length] = opt2;
					opt3 = new Option('Single Shear - Wood Main Member', 'Single Shear');
					scenario.options[scenario.options.length] = opt3;
					opt3 = new Option('Single Shear - Concrete Main Member', 'Single Shear Concrete');
					scenario.options[scenario.options.length] = opt3;
					opt3 = new Option('Double Shear', 'Double Shear');
					scenario.options[scenario.options.length] = opt3;
				}
			}
		}
		
		//--------------------------------------------------------------------------------------
		//fasttype(): This function sets all of the options for the loading scenario 
		//based on what the user selects for the fastener type
		//--------------------------------------------------------------------------------------			
		function fasttype() {
			
			var opt4;
			var connection = document.form1.connection_type;
			var fastener = document.form1.fastener_types;
			var scenario = document.form1.loading_scenario;
			
			
			if (connection != null && fastener != null && scenario != null) {
			// delete all loading_scenario options
			scenario.length = 0
			if (connection.value == "Lateral loading") {
				if (fastener.value == "Bolt") {
					opt4 = new Option('Single Shear - Wood Main Member', 'Single Shear');
					scenario.options[scenario.options.length] = opt4;
					opt4 = new Option('Single Shear - Concrete Main Member', 'Single Shear Concrete');
					scenario.options[scenario.options.length] = opt4;
					opt4 = new Option('Double Shear - Wood Main Member', 'Double Shear');
					scenario.options[scenario.options.length] = opt4;
					opt4 = new Option('Double Shear - Steel Main Member', 'Double Shear Steel');
					scenario.options[scenario.options.length] = opt4;
				}
				else {
					opt4 = new Option('Single Shear', 'Single Shear');
					scenario.options[scenario.options.length] = opt4;
				}	
			}
			else if (connection.value == "Withdrawal loading") {
				opt4 = new Option('N/A', 'N/A');
				scenario.options[scenario.options.length] = opt4;
			}
			}
		}
		
		
		//--------------------------------------------------------------------------------------
		//sm_switch(): This function sets all of the options for the side member thickness
		//based on what the user selects for the side member type
		//--------------------------------------------------------------------------------------	
		var smangle_storage;
		var smthickness_storage;
		function sm_switch() {
   			var opt2;
   			var sidetype = document.form1.sm_type;
   			var sidethick = document.form1.sm_thickness;
   			//if(sidethick == "-1") sidethick = document.form1.sm_thickness_text;
   			var fastener = document.form1.fastener_types.value;
   		
			// delete all options
			if(sidetype != null && sidethick != null) {
				smthickness_storage = sidethick.value;
				sidethick.length = 0;
				
				//if theta angle is not disabled right now then store the value
				if(document.form1.theta_angle_sm != null)
				{
					if(document.form1.theta_angle_sm.disabled == false)
					{
						storagetest = document.form1.theta_angle_sm.value;
					}
				}
				
				if (sidetype.value == "Steel") {
						if(fastener == "Lag Screw" || fastener == "Wood Screw" || fastener == "Nail") {
							opt2 = new Option('20 gage', '0.036');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('18 gage', '0.048');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('16 gage', '0.060');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('14 gage', '0.075');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('12 gage', '0.105');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('11 gage', '0.120');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('10 gage', '0.134');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('7 gage', '0.179');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('3 gage', '0.239');
							sidethick.options[sidethick.options.length] = opt2;
							opt2 = new Option('1/4 in.', '0.25');
							sidethick.options[sidethick.options.length] = opt2;

						}
						else {
							if(fastener == "Bolt")
							{
								opt2 = new Option('20 gage', '0.036');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('18 gage', '0.048');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('16 gage', '0.060');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('14 gage', '0.075');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('12 gage', '0.105');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('11 gage', '0.120');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('10 gage', '0.134');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('7 gage', '0.179');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('3 gage', '0.239');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('1/4 in.', '0.25');
								sidethick.options[sidethick.options.length] = opt2;
							}
							else
							{
								opt2 = new Option('1/4 in.', '0.25');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('3/8 in.', '0.375');
								sidethick.options[sidethick.options.length] = opt2;
								opt2 = new Option('1/2 in.', '0.5');
								sidethick.options[sidethick.options.length] = opt2;
							}
						}
						
						if(document.form1.theta_angle_sm != null) {
							document.form1.theta_angle_sm.value = 0;
							document.form1.theta_angle_sm.disabled = true;
						}
				}
	 			else if (sidetype.value == "Oriented Strand Board (OSB)" || sidetype.value == "Plywood (Structural 1 grade)" || sidetype.value == "Plywood (other grades)") {
						opt2= new Option('3/8 in.', '0.375');
						sidethick.options[sidethick.options.length] = opt2;
						opt2= new Option('7/16 in.', '0.4375');
						sidethick.options[sidethick.options.length] = opt2;
						opt2 = new Option('15/32 in.', '0.46875');
						sidethick.options[sidethick.options.length] = opt2
						opt2= new Option('19/32 in.', '0.59375');
						sidethick.options[sidethick.options.length] = opt2;
						opt2= new Option('23/32 in.', '0.71875');
						sidethick.options[sidethick.options.length] = opt2;
						opt2= new Option('1 in.', '1');
						sidethick.options[sidethick.options.length] = opt2;
						opt2= new Option('1-1/8 in.', '1.125');
						sidethick.options[sidethick.options.length] = opt2;
						opt2= new Option('1-1/4 in.', '1.25');
						sidethick.options[sidethick.options.length] = opt2;
						
						if(document.form1.theta_angle_sm != null) {
							
							document.form1.theta_angle_sm.value = 0;
							document.form1.theta_angle_sm.disabled = true;
						}
				}
				else {
					opt2 = new Option ('0.5 in.', '0.5');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('0.625 in.', '0.625');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('0.75 in.', '0.75');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('1.0 in.', '1.0');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('1.25 in.', '1.25');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('1.5 in.', '1.5');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('1.75 in.', '1.75');
					sidethick.options[sidethick.options.length] = opt2;
					opt2 = new Option ('2.5 in.', '2.5');
					sidethick.options[sidethick.options.length] = opt2;
					if(fastener == "Lag Screw" || fastener == "Bolt") {
						opt2 = new Option ('3.5 in.', '3.5');
						sidethick.options[sidethick.options.length] = opt2;
					}
					opt2 = new Option('-- Other (in inches) --', '-1');
					sidethick.options[sidethick.options.length] = opt2;
					if(document.form1.theta_angle_sm != null)
					{
						document.form1.theta_angle_sm.disabled = false;
						document.form1.theta_angle_sm.value = storagetest;
					}
				}
				resetDropDown(sidethick, smthickness_storage);
			}
		}

		//--------------------------------------------------------------------------------------
		//mm_switch(): This function sets all of the options for the main member thickness
		//based on what the user selects for the main member type. It also sets the options for
		//side member type and then calls sm_switch to set the correct side member thickness
		//options
		//--------------------------------------------------------------------------------------	
		function mm_switch() {
			var opt;
			var opt2;
			var maintype = document.form1.mm_type;
			var mainthick = document.form1.mm_thickness;
			//if(mainthick == "-1") mainthick = document.form1.mm_thickness_text;
			var sidetype = document.form1.sm_type;
			var sidethick = document.form1.sm_thickness;
			//if(sidethick == "-1") sidethick = document.form1.sm_thickness_text;
			
			if(maintype != null && mainthick != null && sidetype != null && sidethick != null) {

			// delete all options
			tempmain = mainthick.value;
			mainthick.length = 0;

				if (maintype.value == "Concrete"){
					opt = new Option('4 in.', '4');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('5 in.', '5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('6 in.', '6');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('7 in.', '7');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('8 in.', '8');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('-- Other (in inches) --', '-1');
					mainthick.options[mainthick.options.length] = opt;
				}
				else if (maintype.value == "Steel"){
					opt = new Option('20 gage', '0.036');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('18 gage', '0.048');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('16 gage', '0.060');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('14 gage', '0.075');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('12 gage', '0.105');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('11 gage', '0.120');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('10 gage', '0.134');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('7 gage', '0.179');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('3 gage', '0.239');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('1/4 in.', '0.25');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('3/8 in.', '0.375');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('1/2 in.', '0.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('5/8 in.', '0.675');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('3/4 in.', '0.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('7/8 in.', '0.875');
					mainthick.options[mainthick.options.length] = opt;
				}
				else if (maintype.value == "Glulam AC" || maintype.value == "Glulam SP" || maintype.value == "Glulam DFL" || maintype.value == "Glulam DFS" || maintype.value == "Glulam HFN" || maintype.value == "Glulam Hem-Fir" || maintype.value == "Glulam SPF" || maintype.value == "Glulam SPFS" || maintype.value == "Glulam WW") {
					opt = new Option('2.5 in.', '2.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('3 in.', '3');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('3.125 in.', '3.125');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('5 in.', '5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('5.125 in.', '5.125');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('6.75 in.', '6.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('8.5 in.', '8.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('8.75 in.', '8.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('10.5 in.', '10.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('10.75 in.', '10.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('12.25 in.', '12.25');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('14.25 in.', '14.25');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('-- Other (in inches) --', '-1');
					mainthick.options[mainthick.options.length] = opt;
				}
				else {
					opt = new Option ('0.75 in.', '0.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('1.5 in.', '1.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('1.75 in.', '1.75');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('2.5 in.', '2.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('3.5 in.', '3.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('5.5 in.', '5.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('7.5 in.', '7.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('9.5 in.', '9.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option ('11.5 in.', '11.5');
					mainthick.options[mainthick.options.length] = opt;
					opt = new Option('-- Other (in inches) --', '-1');
					mainthick.options[mainthick.options.length] = opt;
				}
			resetDropDown(mainthick, tempmain);
		}
	}
	

	//--------------------------------------------------------------------------------------
	//dialength(): This function sets all of the options for the lag screw length
	//based on what the user selects for the fastener diameter
	//--------------------------------------------------------------------------------------	
	function dialength() {
	
	var opt;
	var diameter = document.form1.fast_dia;
	var lslength = document.form1.ls_length;

	if(diameter != null && lslength != null) {
		// delete all options
		tempvalue = lslength.value;
		lslength.length = 0
		
		if (diameter.value == "0.625") {
			opt = new Option('2 in.', '2');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('2.5 in.', '2.5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('3 in.', '3');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('4 in.', '4');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('5 in.', '5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('6 in.', '6');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('7 in.', '7');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('8 in.', '8');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('9 in.', '9');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('10 in.', '10');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('11 in.', '11');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('12 in.', '12');
			lslength.options[lslength.options.length] = opt;
			
			}
			
		else if (diameter.value == "0.75" || diameter.value == "0.875" || diameter.value == "1.0") {
			opt = new Option('3 in.', '3');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('4 in.', '4');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('5 in.', '5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('6 in.', '6');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('7 in.', '7');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('8 in.', '8');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('9 in.', '9');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('10 in.', '10');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('11 in.', '11');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('12 in.', '12');
			lslength.options[lslength.options.length] = opt;
			}

		else if (diameter.value == "1.125" || diameter.value == "1.25") {
			opt = new Option('4 in.', '4');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('5 in.', '5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('6 in.', '6');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('7 in.', '7');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('8 in.', '8');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('9 in.', '9');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('10 in.', '10');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('11 in.', '11');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('12 in.', '12');
			lslength.options[lslength.options.length] = opt;
			}
		else { 
			//if (diameter.value <= "0.5") 
			opt = new Option('1 in.', '1');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('1.5 in.', '1.5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('2 in.', '2');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('2.5 in.', '2.5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('3 in.', '3');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('4 in.', '4');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('5 in.', '5');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('6 in.', '6');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('7 in.', '7');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('8 in.', '8');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('9 in.', '9');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('10 in.', '10');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('11 in.', '11');
			lslength.options[lslength.options.length] = opt;
			opt = new Option('12 in.', '12');
			lslength.options[lslength.options.length] = opt;
		}
		resetDropDown(lslength, tempvalue);
	}	
	}
	
	//--------------------------------------------------------------------------------------
	//nailType(): This function sets all of the options for the nail size
	//based on what the user selects for the nail type
	//--------------------------------------------------------------------------------------	
	function nailType() {
	
	var opt;
	var type = document.form1.fast_dia;
	var size = document.form1.nail_size;
	if(type != null && size != null){
	
	// delete all options
		tempvalue = size.value;
		size.length = 0

	if (type.value == "common") {
			opt = new Option('6d (D = 0.113 in.; L = 2 in.)', '6d');
			size.options[size.options.length] = opt;
			opt = new Option('7d (D = 0.113 in.; L = 2.25 in.)', '7d');
			size.options[size.options.length] = opt;
			opt = new Option('8d (D = 0.131 in.; L = 2.5 in.)', '8d');
			size.options[size.options.length] = opt;
			opt = new Option('10d (D = 0.148 in.; L = 3 in.)', '10d');
			size.options[size.options.length] = opt;
			opt = new Option('12d (D = 0.148 in.; L = 3.25 in.)', '12d');
			size.options[size.options.length] = opt;
			opt = new Option('16d (D = 0.162 in.; L = 3.5 in.)', '16d');
			size.options[size.options.length] = opt;
			opt = new Option('20d (D = 0.192 in.; L = 4 in.)', '20d');
			size.options[size.options.length] = opt;
			opt = new Option('30d (D = 0.207 in.; L = 4.5 in.)', '30d');
			size.options[size.options.length] = opt;
			opt = new Option('40d (D = 0.225 in.; L = 5 in.)', '40d');
			size.options[size.options.length] = opt;
			opt = new Option('50d (D = 0.244 in.; L = 5.5 in.)', '50d');
			size.options[size.options.length] = opt;
			}
		else if (type.value == "box") {
			opt = new Option('6d (D = 0.099 in.; L = 2 in.)', '6d');
			size.options[size.options.length] = opt;
			opt = new Option('7d (D = 0.099 in.; L = 2.25 in.)', '7d');
			size.options[size.options.length] = opt;
			opt = new Option('8d (D = 0.113 in.; L = 2.5 in.)', '8d');
			size.options[size.options.length] = opt;
			opt = new Option('10d (D = 0.128 in.; L = 3 in.)', '10d');
			size.options[size.options.length] = opt;
			opt = new Option('12d (D = 0.128 in.; L = 3.25 in.)', '12d');
			size.options[size.options.length] = opt;
			opt = new Option('16d (D = 0.135 in.; L = 3.5 in.)', '16d');
			size.options[size.options.length] = opt;
			opt = new Option('20d (D = 0.148 in.; L = 4 in.)', '20d');
			size.options[size.options.length] = opt;
			opt = new Option('30d (D = 0.148 in.; L = 4.5 in.)', '30d');
			size.options[size.options.length] = opt;
			opt = new Option('40d (D = 0.162 in.; L = 5 in.)', '40d');
			size.options[size.options.length] = opt;
			}
		else if (type.value == "sinker") {
			opt = new Option('7d (D = 0.099 in.; L = 2.125 in.)', '7d');
			size.options[size.options.length] = opt;
			opt = new Option('8d (D = 0.113 in.; L = 2.375 in.)', '8d');
			size.options[size.options.length] = opt;
			opt = new Option('10d (D = 0.120 in.; L = 2.875 in.)', '10d');
			size.options[size.options.length] = opt;
			opt = new Option('12d (D = 0.135 in.; L = 3.125 in.)', '12d');
			size.options[size.options.length] = opt;
			opt = new Option('16d (D = 0.148 in.; L = 3.25 in.)', '16d');
			size.options[size.options.length] = opt;
			opt = new Option('20d (D = 0.177 in.; L = 3.75 in.)', '20d');
			size.options[size.options.length] = opt;
			opt = new Option('30d (D = 0.192 in.; L = 4.25 in.)', '30d');
			size.options[size.options.length] = opt;
			opt = new Option('40d (D = 0.207 in.; L = 4.75 in.)', '40d');
			size.options[size.options.length] = opt;
			opt = new Option('60d (D = 0.244 in.; L = 5.75 in.)', '60d');
			size.options[size.options.length] = opt;
		}
		resetDropDown(size, tempvalue);
		}
	}
	
	
	// set some variables to find which browser is being used
	var isIE=document.all?true:false;
	var isNS4=document.layers?true:false;
	var isNS6=navigator.userAgent.indexOf("Gecko")!=-1?true:false;
	
	//--------------------------------------------------------------------------------------
	//clearright(): This function removes the right drop down menus from the screen
	//--------------------------------------------------------------------------------------	
	
	function clearright()
	{
		var _obj = null;
		
		if(document.getElementById)
		{
			_obj = document.getElementById("rightdropdowns");
		}
		else if(document.layers)
		{
			document.layers["rightdropdowns"].visibility = "hidden";
		}
		else
		{
			window.location.href="error.html";
		}
		
		if(_obj)
		{
			_obj.innerHTML = "";
		}
	
		hidesubmits();
		
		//if we remove the right side let's remove the bottom answers too
		clearbottom();
	}
	
	function hidesubmits()
	{
		var table;
		table = document.getElementById("Table1");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table2");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table3");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table4");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table5");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table6");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table7");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table9");
		if(table != null) table.style.display = "none";
		table = document.getElementById("Table10");
		if(table != null) table.style.display = "none";
		
	}
	//--------------------------------------------------------------------------------------
	//popup(): This function pops up information about each section of the calc
	//--------------------------------------------------------------------------------------	
	function popup(spanArg)
	{
		if(document.getElementById)
			myarg = document.getElementById(spanArg.id);
		else if(document.layers)
			myarg = document.layers[spanArg.id];
		else
			window.location.href="error.html";
			
		var str = '';
		var title = myarg.innerHTML;
		
		if(myarg.id == "ConnectionType")
			str = title + "\n\nWithdrawal loading pulls the fastener directly out of a wood member.  Lateral loading tends to bend the fastener at the shear plane between members.";
		else if(myarg.id == "FastenerType")
			str = title + "\n\nBolts or lag screws per ANSI/ASME B18.2.1. Wood screws per ANSI/ASME B.16.1. Nails per ASTM F1667."
		else if(myarg.id == "LoadingScenario")
			str = title + "\n\nA fastener loaded laterally by two members is in single shear.  A fastener loaded laterally by three members is typically in double shear.";
		else if(myarg.id == "DesignMethod")
			str = title + "\n\nTraditional ASD methods apply all safety adjustments to material strength properties.  LRFD methods apply some safety adjustments to material strength properties and some safety adjustments to code-specified design loads.";
			
		else if(myarg.id == "AngleOfLoadToGrainMain")
			str = title + "\n\nThe angle between the load vector and the longitudinal axis of the wood main member at a connection.";
		else if(myarg.id == "AngleOfLoadToGrainSide")
			str = title + "\n\nThe angle between the load vector and the longitudinal axis of the wood side member at a connection.";
		else if(myarg.id == "LoadDurationFactor")
			str = title + "\n\nAdjusts for the cumulative duration of the connection design load, per NDS Chapter 2, Chapter 10, and Appendix B.";
		else if(myarg.id == "TimeEffectFactor")
			str = title + "\n\nAdjusts for the duration of the principal transient load in the governing LRFD connection load combination per NDS Chapter 2, Chapter 10, and Appendix N.";
		else if(myarg.id == "WetServiceFactor")
			str = title + "\n\nReduction factor for connections in unseasoned lumber or connections exposed to wet service conditions, per NDS Chapter 10.";
		else if(myarg.id == "TemperatureFactor")
			str = title + "\n\nReduction factor for connections with sustained exposure to temperatures above 100 degrees(F), per NDS Chapter 10.";
		else if(myarg.id == "EndGrainFactor")
			str = title + "\n\nReduction factor for lag screws, wood screws, or nails inserted into the end grain of a wood member, per NDS Chapter 11.";
		else if(myarg.id == "DiaphragmFactor")
			str = title + "\n\nA diaphragm factor of 1.1 applies ONLY for nails that connect sheathing to framing members in wood diaphragms and shear walls, per NDS Chapter 11.";
			
		else if(myarg.id == "MainMemberTypeLBD")
			str = title + "\n\nThe middle (inner) member in a three-member connection.";
		else if(myarg.id == "SideMemberTypeLBD")
			str = title + "\n\nOne of the outer members in a three-member connection.";
			
		else if(myarg.id == "MainMemberTypeLBS")
			str = title + "\n\nThe thicker member in a two-member connection.";
		else if(myarg.id == "SideMemberTypeLBS")
			str = title + "\n\nThe thinner member in a two-member connection.";
		else if(myarg.id == "MainMemberTypeLBSC")
			str = title + "\n\nFor lateral loading on bolts in wood-to-concrete connections, concrete is the main member.";
		else if(myarg.id == "SideMemberTypeLBSC")
			str = title + "\n\nFor lateral loading on bolts in wood-to-concrete connections, the wood member is the side member.";
		else if(myarg.id == "MainMemberTypeLLSS")
			str = title + "\n\nThe member holding the point of the lag screw.";
		else if(myarg.id == "SideMemberTypeLLSS")
			str = title + "\n\nThe member closest to the head of the lag screw.";
		else if(myarg.id == "NominalDiameterLLSS")
			str = title + "\n\nThe diameter of the unthreaded shank of the lag screw, per NDS Appendix L and ANSI/ASME B.18.2.1.";
		else if(myarg.id == "LagScrewLengthLLSS")
			str = title + "\n\nThe overall length of the threads and shank of the lag screw (not including the head), per NDS Appendix L and ANSI/ASME B.18.2.1.";
			
		else if(myarg.id == "MainMemberTypeLWSS")
			str = title + "\n\nThe member holding the point of the wood screw.";
		else if(myarg.id == "SideMemberTypeLWSS")
			str = title + "\n\nThe member closest to the head of the wood screw.";
		else if(myarg.id == "WoodScrewNumberLWSS")
			str = title + "\n\nWood screw identification number, per NDS Appendix L and ANSI/ASME B.18.6.1.";
		else if(myarg.id == "WoodScrewLengthLWSS")
			str = title + "\n\nThe total length of the wood screw, per NDS Appendix L and ANSI/ASME B.18.6.1.";
			
		else if(myarg.id == "MainMemberTypeLNS")
			str = title + "\n\nThe member holding the point of the nail.";
		else if(myarg.id == "SideMemberTypeLNS")
			str = title + "\n\nThe member closest to the head of the nail.";
		else if(myarg.id == "NailTypeLNS")
			str = title + "\n\nEither common, box, or sinker nails in accordance with NDS Appendix L and ASTM F1667.";
		else if(myarg.id == "NailSizeLNS")
			str = title + "\n\nPennyweight classification for nails, per NDS Appendix L and ASTM F1667.";
		alert(str);
		
	}
	
	//--------------------------------------------------------------------------------------
	//clearbottom(): This function removes the bottom "answers" from the screen
	//--------------------------------------------------------------------------------------	
	
	function clearbottom()
	{
		var _obj = null;
		
		if(document.getElementById)
		{
			_obj = document.getElementById("bottomoutput");
		}
		else if(document.layers)
		{
			document.layers["bottomoutput"].visibility = "hidden";
		}
		else
		{
			window.location.href="error.html";
		}
		
		if(_obj)
		{
			_obj.innerHTML = "";
		}
	}
	
	//--------------------------------------------------------------------------------------
	//checkMainValue(): This function checks the value of the Main Member Thickness dropdown
	//in it's onChange event to see if the value is -1. If it is, that means the user wants to
	//enter the Main Member Thickness by hand, so we will provide a textbox for them
	//--------------------------------------------------------------------------------------
	function checkMainValue()
	{
		if(!document.form1.mm_thickness)
			return;
		var mainThicknessValue = document.form1.mm_thickness.value;
		//alert(mainThicknessValue);
		if(mainThicknessValue == "-1")
		{
			document.form1.mm_thickness_text.style.display = "block";
		}
		else
		{
			document.form1.mm_thickness_text.style.display = "none";
		}
	}	
	
	//--------------------------------------------------------------------------------------
	//checkSideValue(): This function checks the value of the Side Member Thickness dropdown
	//in it's onChange event to see if the value is -1. If it is, that means the user wants to
	//enter the Side Member Thickness by hand, so we will provide a textbox for them
	//--------------------------------------------------------------------------------------
	function checkSideValue()
	{
		if(!document.form1.sm_thickness)
			return;
		var sideThicknessValue = document.form1.sm_thickness.value;
		//alert(sideThicknessValue);
		if(sideThicknessValue == "-1")
		{
			document.form1.sm_thickness_text.style.display = "block";
		}
		else
		{
			document.form1.sm_thickness_text.style.display = "none";
		}
	}	