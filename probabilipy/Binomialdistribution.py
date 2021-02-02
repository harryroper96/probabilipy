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
        Distribution.__init__(self)
        self.p = p
        self.n = n
        self.calculate_mean()
        self.calculate_stdev()
    
    def read_data(self, file_name):
        
        """Function to read in data from a .txt file. File should contain one float per line.
        Each float should take the value of either 0 (indicating failure) or 1.0 (indicating success).
        
        Args:
            file_name (string): file to read data from
        
        Returns:
            None
            
        """
        
        Distribution.read_data(self, file_name)
        self.p = float(sum(self.data)) / len(self.data)
        self.n = len(self.data)
        self.calculate_mean()
        self.calculate_stdev()
    
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
    
    def calculate_stdev(self):
        
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
        
        """Function to calculate the probability that a given (x) number of successful
        trials will be observed.
        
        Args:
            x (int): the number of successful trials of which to calculate the probability
        
        Returns:
            float: the value of the probability mass function at x
        
        """
        
        return (math.factorial(self.n) / (math.factorial(x) * math.factorial(self.n - x))) \
                * self.p ** x * (1 - self.p) ** (self.n - x)
    
    def cdf(self, x):
        
        """Function to calculate the probability that the number of successful trials observed
        will be less than or equal to the given x value or between the given x interval.
        
        Args:
            x (int or tuple of ints): the x value of interval below/between which to 
                calculate the probability
        
        Returns:
            float: CDF of the data set's distribution below/between x
        
        """
        
        if type(x) is tuple:
            try:
                assert len(x) == 2, 'x must be a tuple of length 2 to calculate \
                probability between interval'
            except AssertionError as error:
                raise
            
            try:
                assert x[1] > x[0], 'second term in interval must be greater than first'
            except AssertionError as error:
                raise
            
            return sum([self.pmf(i) for i in range(x[0], x[1] + 1)])
        
        else:
            return sum([self.pmf(i) for i in range(x + 1)])
    
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
        result = Binomial()
        result.n = self.n + other.n
        result.p = self.p
        result.calculate_mean()
        result.calculate_stdev()
        
        return result
    
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial instance
        
        """
        
        return "mean {}, standard deviation {}, p {}, n {}".\
        format(self.mean, self.stdev, self.p, self.n)