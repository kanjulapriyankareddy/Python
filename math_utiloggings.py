import logging
import os


log_dir= "loggings"
log_file_name="app.log"

os.makedirs(log_dir, exist_ok=True)
log_path=os.path.join(log_dir,log_file_name)

logging.basicConfig(filename=log_path,level=logging.INFO,format="[%(asctime)s] %(name)s- %(levelname)s-%(message)s",force=True)


def add(a,b):
    result=a+b
    logging.info(f"adding {a}+{b}={result}")
    return result

def sub(a,b):
    result= a-b
    logging.info(f"subtraction {a}-{b}={result}")
    return result

def multiply(a,b):
    result=a*b
    logging.info(f"multiplicatin {a} *{b}={result}")
    return result    
multiply(10,20)

def divide(a,b):
    try:
        result=a/b
        logging.debug(f"dividing {a} /{b}={result}")
        return result
    except ZeroDivisionError:
        logging.error("division by zero error")
        return None