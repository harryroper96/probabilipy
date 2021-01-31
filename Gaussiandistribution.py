import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Gaussian(Distribution):
    
    """Gaussian distribution class for analysing a Gaussian probability distribution.
        
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
    """
    
    def __init__(self, mu=0, sigma=1):
        Distribution.__init__(mu, sigma)
    
    def calculate_mean(self):
        
        """Function to calculate the mean of the data set.
        
        Args:
            None
        
        Returns:
            float: mean of the data set
        
        """
        
        mean = float(sum(self.data)) / len(self.data)
        self.mean = mean
        return self.mean
    
    def calculate_stdev(self, sample=True):
        
         """Function to calculate the standard deviation of the data set.
        
        Args:
            sample (bool): whether data set represents a sample or a population
        
        Returns:
            float: standard deviation of the data set
        
        """
        
        if sample:
            n = float(len(self.data)) - 1
        else:
            n = float(len(self.data))
        sq_diffs = [(i - self.mean) ** 2 for i in self.data]
        sigma = math.sqrt(sum(sq_diffs) / n)
        self.stdev = sigma
        return self.stdev
    
    def plot_dist(self, bins=50):
        
        """Function to plot a histogram of the distribution of the data set using
        matplotlib's pyplot library.
        
        Args:
            None
        
        Returns:
            None
        
        """
        
        plt.hist(self.data, bins=bins)
        plt.title('Gaussian Distribution')
        plt.xlabel('Variable')
        plt.ylabel('Frequency')
    
    def pdf(self, x):
        
        """Function to calculate the probability density function of the data set's
        distribution at a given x value.
        
        Args:
            x (float): x value at which to calculate the probability density
        
        Returns:
            float: PDF of the data set's distribution at x
        
        """
        
        return (1.0 / (self.stdev * math.sqrt(2 * math.pi))) * \
                math.e ** (-0.5 * ((x - self.mean) / self.stdev) ** 2)
    
    def cdf(self, x, interval=False):
        
        """Function to calculate the probability that a random variable in the data set
        will take a value either less than or equal to a given x value or between a
        given interval of x values.
        
        Args:
            x (float or tuple of floats): the x value of interval below/between which to 
                calculate the probability
            interval (bool): whether x represents an interval or a single value
        
        Returns:
            float: CDF of the data set's distribution below/between x
        
        """
        
        if interval:
            try:
                assert len(x) == 2, 'x must be a tuple of length 2 to calculate \
                probability between interval'
            except AssertionError as error:
                raise
            
            try:
                assert x[1] > x[0], 'second term in interval must be greater than first'
            except AssertionError as error:
                raise
            
            return (0.5 * (1.0 + math.erf((x[1] - self.mean) / (self.stdev * math.sqrt(2))))) \
                    - (0.5 * (1.0 + math.erf((x[0] - self.mean) / (self.stdev * math.sqrt(2)))))
        
        else:
            return (0.5 * (1.0 + math.erf((x - self.mean) / (self.stdev * math.sqrt(2)))))