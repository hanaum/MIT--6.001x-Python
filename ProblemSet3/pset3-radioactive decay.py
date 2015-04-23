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

radiationExposure(0.0, 4.0, 0.25)
