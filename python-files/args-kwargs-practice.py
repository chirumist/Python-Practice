"""
Args and kwargs perameaters are optinal
args type is tupple and kwags are dic type
"""


def list_function(normal,*args,**kwargs):
    # print(type(normal),type(args),type(kwargs))
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(key,": - :",value)



testNormal = "Im the one of noob in gta."
her = ["chiarga", "test", "brow-code"]

her1 = {"chiarga" : "Good boy", "test" : "testing", "brow-code" : "test bros"}
list_function(testNormal, *her, **her1)
