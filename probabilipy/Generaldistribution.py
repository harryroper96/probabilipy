class Distribution():
    
    def __init__(self, mu=0, sigma=1):
        
        """Generic distribution class for analysing a probability distribution.
        
        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
        """
        
        self.mean = mu
        self.stdev = sigma
        self.data = []
    
    def read_data(self, file_name):
        
        """Function to read in data from a .txt file.
        File should contain one float per line.
        
        Args:
            file_name (string): file to read data from
        
        Returns:
            None
            
        """
        
        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(float(line))
                line = file.readline()
        file.close()
        
        self.data = data_list
        self.calculate_mean()
        self.calculate_stdev()