from math import *

def haversine(r,sig1,lamb1,sig2,lamb2):
    sig1_rad = radians(sig1)
    sig2_rad = radians(sig2)
    lamb1_rad = radians(lamb1)
    lamb2_rad = radians(lamb2)
    
    p0 = (sin((sig2_rad-sig1_rad)/2))*(sin((sig2_rad-sig1_rad)/2))
    p1 = (sin((lamb2_rad-lamb1_rad)/2))*(sin((lamb2_rad-lamb1_rad)/2))
    p2 = cos(sig1_rad)*cos(sig2_rad)*p1
    p3 = (p0+p2)**0.5
    d = 2*r*asin(p3)
    return d
