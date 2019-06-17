from PIL import Image

class ElevationMap:
    """Elevation map is a class that takes a matrix (list of lists, 2D) of 
    integers and can be used to generate an image fo those elevations like a 
    standard elevation map.
    """
    def __init__(self, elevations):
        self.elevations = elevations
    
    def elevation_at_coordinate(self, x, y):
        """Using the image coordinates to look up and return the corresponding
        elevation value within the elevations array. To do this method, account for
        flipping x and y coordinates to translate from image to array"""
        return self.elevations[y][x]
    
    def min_elevation(self):
        """Goes through each row and finds min, then finds min of those. Seems like 
        there would be a better way?
        """
        return min([min(row) for row in self.elevations])
        
    def max_elevation(self):
        """Same as above, but for max
        """
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y):
        """Given an x, y coordinate, return the intensity level (used for grayscale
        of an image) of the elevation at that coordinate"""
        elevation = self.elevation_at_coordinate(x, y)
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()
        return (elevation - min_elevation) / (max_elevation - min_elevation)

def draw_grayscale_gradient(filename, width, height):
    image = Image.new(mode='L', size=(width, height))
    for x in range(width):
        for y in range(height):
            image.putpixel((x, y), (int(x / width * 255))
        image.save(filename)

if __name__ == "__main__":
    
    elevations = read_file_into_ints('elevation_small.txt')
    e_map = ElevationMap(elevations)

    e_map.draw_grayscale_gradient('map.png', 600, 600)