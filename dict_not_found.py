def get_something(key, dictionary):
    '''This is a dictionary used to test int value key return not found'''
    # key = str(key)
    try:
        if not type(key) is int:
            raise TypeError ("only integers are allowed, you used") # key == type(int)
        #print(type(key))
    except TypeError as N:
        print(N)
    except Exception as e:
           print(type(key) + e)
    else:
        if key in a_dict:
            read_dict = dictionary[key]
            print(read_dict)
        elif not key in a_dict == True:
            print("not found")           
#    finally:
#        print("Final case hit")


a_dict = {1 : "Definition 1", 2 : "Definition 2", 3 : "Definition 3"}
