import numpy as np

def calculate(list):
    global arr
    
    try:    arr = np.array(list).reshape(3, 3)
    except: raise ValueError("List must contain nine numbers.")

    ops = {'mean': 'mean', 'variance': 'var', 'standard deviation':'std', 'max':'max', 'min':'min', 'sum':'sum'}

    calculations = {
        i : eval(f"[[*arr.{ops[i]}(axis=0)], [*arr.{ops[i]}(axis=1)], arr.{ops[i]}()]") for i in ops
    }

    return calculations