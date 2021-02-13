# Imports
from json import load as json_load
from termcolor import cprint #optional - pip install termcolor
try: from settings import logging, debug_mode, json_code_file
except ImportError:
   logging = True
   debug_mode = True
   json_code_file = 'logging/debug_codes.json'

# Configuration
log_type_info = ['i','info','information','1',1]
log_type_warn = ['w','warn','warning','2',2]
log_type_error = ['e','err','error','3',3]
log_type_console = ['c','cmd','console','app','sys','system','0',0]
log_type_debug = ['d','debug','-1',-1]

# Functions
def log(log_type,log_code):
   if logging == True: 
      code_file = open(json_code_file)
      log_file = json_load(code_file)

      if log_type in log_type_info:
         log_type = 'info'
         log_title = 'INFO'
         log_color = 'white'
      elif log_type in log_type_warn:
         log_type = 'warn'
         log_title = 'WARN'
         log_color = 'yellow'
      elif log_type in log_type_error:
         log_type = 'error'
         log_title = 'ERROR'
         log_color = 'red'
      elif log_type in log_type_console:
         log_type = 'console'
         log_title = 'APP'
         log_color = 'blue'
      elif log_type in log_type_debug:
         if debug_mode == True:
            log_type = 'debug'
            log_title = 'DEBUG'
            log_color = 'magenta'
      else:
         try: cprint('-'+'\n'+'[ERROR]: Could not log. '+'\n'+'Log Type: '+str(log_type)+'\n'+'Log Code: '+str(log_code)+'\n'+'-', 'red')
         except SyntaxError or NameError: print('[ERROR]: Could not log. '+'\n'+'Log Type: '+str(log_type)+'\n'+'Log Code: '+str(log_code))
      for code,value in log_file[log_type].items():
         if int(log_code) == int(code):
            try: cprint(('['+log_title+' #'+str(log_code)+']: '+value),log_color)
            except SyntaxError or NameError: 
               print('['+log_title+' #'+str(log_code)+']: '+value)
            return
   else: pass
