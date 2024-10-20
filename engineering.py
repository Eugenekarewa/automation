def  socialgathering(victiminfo):
     lure=f""" Hi my name is {victiminfo['name']}. I recently lost my phone and need to renew my sim card on a new phone .
               Here are the details that are required for verification purposes
               - Full Name : {victiminfo['name']}
               -Date of Birth: {victiminfo['dob']}
               - Address:{victiminfo['address']}
               -Last 4 digits of SSN :{victiminfo['ssn']}
 

     """
     return lure
#usage
victiminfo={
   'name':'Eugene Karewa',
   'dob' :'24/10/2000',
   'address':'a place cooler than you think',
   'ssn':'9045'
}
lure=socialgathering(victiminfo)
print("running the code 557 on the target:")
print(lure)

