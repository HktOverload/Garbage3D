# Kaidun (by HktOverload)

import abc, math

from geom import *

# The top-level functions should not be imported using star
__all__ = 'Light PointLight'.split()

class Light(abc.ABC):

    @abc.abstractmethod
    def intensity(self, target):
        pass

class PointLight(Light):
    def __init__(self, ctr, brightness):
        self.ctr = ctr
        self.brightness = brightness
    
    def intensity(self, target):
        dist = math.hypot(add(target, neg(self.ctr)))
        return self.brightness * (1 / (dist ** 2)) # inv-square law

def lambertian(geom):
    return geom.withData()