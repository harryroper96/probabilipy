import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Poisson(Distribution):
    
    """Poisson distribution class for analysing a Poisson probability distribution.
        
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats extracted from the data file
        m (float) representing the average number of occurences in the given period
    """
    
    def __init__(self, m=2.5):
        Distribution.__init__(self)
        self.m = m
        self.calculate_mean()
        self.calculate_stdev()
    
    def read_data(self, file_name):
        
        """Function to read in data from a .txt file. File should contain one float per line.
        Each line should indicate the number of occurences in the given period.
        
        Args:
            file_name (string): file to read data from
        
        Returns:
            None
            
        """
        
        Distribution.read_data(self, file_name)
        self.m = float(sum(self.data)) / len(self.data)
        self.calculate_mean()
        self.calculate_stdev()
    
    def calculate_mean(self):
        
        """Function to calculate the mean of the data set from its
        m value.
        
        Args:
            None
        
        Returns:
            float: mean of the data set
        
        """
        
        mean = self.m
        self.mean = mean
        return self.mean
    
    def calculate_stdev(self):
        
        """Function to calculate the standard deviation of the data set
         from its p and n values.
        
        Args:
            None
        
        Returns:
            float: standard deviation of the data set
        
        """
        
        sigma = math.sqrt(self.m)
        self.stdev = sigma
        return self.stdev
    
    def plot_dist(self, bins=None):
        
        """Function to plot a histogram of the distribution of the data set using
        matplotlib's pyplot library.
        
        Args:
            bins (int): number of bins the histogram should include
        
        Returns:
            None
        
        """
        
        plt.hist(self.data, bins=bins)
        plt.title('Poisson Distribution')
        plt.xlabel('Variable')
        plt.ylabel('Frequency')
    
    def pmf(self, k):
        
        """Function to calculate the probability that a given (k) number of occurences will be observed.
        
        Args:
            k (int): the number of occurences of which to calculate the probability
        
        Returns:
            float: the value of the probability mass function at k
        
        """
        
        return (self.m ** k * math.exp(-self.m)) / math.factorial(k)
    
    def cdf(self, k):
        
        """Function to calculate the probability that the number of occurences observed
        will be less than or equal to the given k value or between the given k interval.
        
        Args:
            k (int or tuple of ints): the k value of interval below/between which to 
                calculate the probability
        
        Returns:
            float: CDF of the data set's distribution below/between k
        
        """
        
        if type(k) is tuple:
            try:
                assert len(k) == 2, 'k must be a tuple of length 2 to calculate \
                probability between interval'
            except AssertionError as error:
                raise
            
            try:
                assert k[1] > k[0], 'second term in interval must be greater than first'
            except AssertionError as error:
                raise
            
            return sum([self.pmf(i) for i in range(k[0], k[1] + 1)])
        
        else:
            return sum([self.pmf(i) for i in range(k + 1)])
    
    def __add__(self, other):
        
        """Function to add together two Poisson distributions
        
        Args:
            other (Poisson): Poisson instance
            
        Returns:
            Poisson: Poisson distribution
            
        """
        
        result = Poisson()
        result.m = self.m + other.m
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
    
    def __repr__(self):
    
        """Function to output the characteristics of the Poisson instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Poisson instance
        
        """
        
        return "mean {}, standard deviation {}, m {}".\
        format(self.mean, self.stdev, self.m)