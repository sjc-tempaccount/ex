#!/usr/bin/python
"""
Functions to do temperature conversions

"""
def ctof(ctemp):
    """
    convert a temperature in Celsius to Fahrenheit
    """
    ftemp = (ctemp * 9/5) + 32

    # return
    return ftemp


def ftoc(ftemp):
    """
    convert a temperature in Fahrenheit  to Celsius
    """
    ctemp = (ftemp - 32) * 5/9

    # return
    return ctemp


def main():
    """
    Code to only be run when the module is run and not on import
    """
    print(f"3 Celsius is {ctof(3):0.2f} Fahrenheit")
    print(f"3 Fahrenheit is {ftoc(3):0.2f} Celsius")

if __name__ == "__main__":
    main()




    
