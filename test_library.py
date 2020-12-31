import code_library
import inspect

if "code_library" in locals():
    str = input()
    obj = ".".join(["code_library", str])
    
    try:
        print(inspect.getsource(eval(obj)))
        #print(open(my_library.__file__).read())
    except OSError:
        print("Source not available, possibly a C module.")
else:
    print('you havn"t imported the library  ')


