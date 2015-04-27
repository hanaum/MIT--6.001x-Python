'''Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.

MIT-6.001x Python
Hana Um
'''

# pre-defined curve function for radiation
def f(x):
    import math
    return 400*math.e**(math.log(0.5)/3.66 * x)


def radiationExposure(start, stop, step):
    total_exposure = 0
    time = start
    while time < stop:
        total_exposure += step * f(time)
        time += step
    return total_exposure

#test arguments
radiationExposure(0.0, 4.0, 0.25)
