import sys  #sys Python ka built-in module hai...
#system-related information deta hai
# errors ki details nikalne me help karta hai
import logging


def error_message_detail(error,error_detail:sys): #Function Definition
# Ye function:error ki complete detail banata hai
# Parameters are error(actual error) and error_detail(system error details)

    _,_,exc_tb=error_detail.exc_info() #exc_info() error ki details return karta hai...
    #exc_tb = traceback Ye batata hai k error kis line me aya r kis file me aya
    #python me _ ka matlab:“Ye value mujhe use nahi karni”

    file_name=exc_tb.tb_frame.f_code.co_filename #Ye line:jis file me error aya uska naam nikalti hai
    error_message="Error occured in python script name[{0}] line number[{1}] error message[{2}]".format #Custom error message banana.
    (
    file_name,exc_tb.tb_lineno,str(error))
    return error_message
    

class CustomException(Exception): #Ye apni khud ki custom error class bana raha hai...and exception 
    # means k ya Python ki original Exception class ko extend kar rahe hain.
    def __init__(self, error_message,error_detail:sys): #constructor
        super().__init__(error_message)  
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self): # string method jbh error print hoga tou ya method chla ga
        return self.error_message # return me Detailed message show hoga.
if __name__=="__main__":

    try:
        a=1/10
    except Exception as e:
        logging.info("Divided by zero")
        raise CustomException(e,sys)