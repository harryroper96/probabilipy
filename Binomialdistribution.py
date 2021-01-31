import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    
    """Binomial distribution class for analysing a Binomial probability distribution.
        
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
        p (float) representing the probability of a successful outcome
        n (int) representing the number of trials
    """
    
    def __init__(self, p=0.5, n=10):
        Distribution.__init__(p, n)
        self.p = p
        self.n = n
    
    def read_data(self, file_name):
        
        """Function to read in data from a .txt file. File should contain one float per line.
        Each float should take the value of either 0 (indicating failure) or 1.0 (indicating success).
        
        Args:
            file_name (string): file to read data from
        
        Returns:
            None
            
        """
        
        Distribution.read_data(file_name)
        self.p = float(sum(self.data)) / len(self.data)
        self.n = len(self.data)
    
    def calculate_mean(self):
        
        """Function to calculate the mean of the data set from its
        p and n values.
        
        Args:
            None
        
        Returns:
            float: mean of the data set
        
        """
        
        mean = self.p * self.n
        self.mean = mean
        return self.mean
    
    def calculate_stdev(self, sample=True):
        
         """Function to calculate the standard deviation of the data set
         from its p and n values.
        
        Args:
            None
        
        Returns:
            float: standard deviation of the data set
        
        """
        
        sigma = math.sqrt(self.n * self.p * (1 - self.p))
        self.stdev = sigma
        return self.stdev
    
    def plot_dist(self):
        
        """Function to plot a histogram of the distribution of the data set using
        matplotlib's pyplot library.
        
        Args:
            None
        
        Returns:
            None
        
        """
        
        plt.bar([0, 1], [self.data.count(0), self.data.count(1)])
        plt.title('Binomial Distribution')
        plt.xlabel('Variable')
        plt.ylabel('Frequency')
    
    def pmf(self, x):
        pass