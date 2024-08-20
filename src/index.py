# Geographical Boundaires:

# Size & Shape:
class Airspace:
    def __init__(self, name, length, width, height, alt):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.alt = alt

    def __repr__(self):
        return (f"Airspace(Name='{self.name}', Length={self.length}, "
                f"Width={self.width}, Height={self.height}, "
                f"Altitude={self.alt})")

airspace_one = Airspace(name='LDN', length=25, width=10, height=20, alt=40)

print(airspace_one)