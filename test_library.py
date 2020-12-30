import inspect
import my_library



try:    
    print (inspect.getsource(my_library.add))
    #print(open(my_library.__file__).read())
except OSError:
    print("Source not available, possibly a C module.")
