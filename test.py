import unittest

from probabilipy import Gaussian, Binomial, Poisson

class TestGaussianClass(unittest.TestCase):
    def setUp(self):
        self.gaussian = Gaussian(25, 2)
        self.gaussian.read_data('gaussian_test.txt')

    def test_meancalculation(self): 
        self.assertEqual(round(self.gaussian.calculate_mean(), 2), 4.62)
        
    def test_stdevcalculation(self):
        self.assertEqual(round(self.gaussian.calculate_stdev(), 2), 2.67)

    def test_pdf(self):
        self.assertEqual(round(self.gaussian.pdf(5), 2), 0.15)
    
    def test_cdf_single(self):
        self.assertEqual(round(self.gaussian.cdf(5), 2), 0.56)
    
    def test_cdf_interval(self):
        self.assertEqual(round(self.gaussian.cdf((2, 5)), 2), 0.39)

    def test_add(self):
        gaussian_one = Gaussian(25, 3)
        gaussian_two = Gaussian(30, 4)
        gaussian_sum = gaussian_one + gaussian_two
        
        self.assertEqual(gaussian_sum.mean, 55)
        self.assertEqual(gaussian_sum.stdev, 5)
        
class TestBinomialClass(unittest.TestCase):
    def setUp(self):
        self.binomial = Binomial()
        self.binomial.read_data('binomial_test.txt')
    
    def test_calculatemean(self):
        mean = self.binomial.calculate_mean()
        self.assertEqual(mean, 9)
    
    def test_calculatestdev(self):
        stdev = self.binomial.calculate_stdev()
        self.assertEqual(round(stdev, 2), 2.22)
        
    def test_pmf(self):
        self.assertEqual(round(self.binomial.pmf(12), 2), 0.07)
    
    def test_cdf_single(self):
        self.assertEqual(round(self.binomial.cdf(7), 2), 0.25)
    
    def test_cdf_interval(self):
        self.assertEqual(round(self.binomial.cdf((8, 12)), 2), 0.69)

    def test_add(self):
        binomial_one = Binomial(.4, 20)
        binomial_two = Binomial(.4, 60)
        binomial_sum = binomial_one + binomial_two
        
        self.assertEqual(binomial_sum.p, .4)
        self.assertEqual(binomial_sum.n, 80)

class TestPoissonClass(unittest.TestCase):
    def setUp(self):
        self.poisson = Poisson()
        self.poisson.read_data('poisson_test.txt')
    
    def test_calculatemean(self):
        mean = self.poisson.calculate_mean()
        self.assertEqual(mean, 6.35)
    
    def test_calculatestdev(self):
        stdev = self.poisson.calculate_stdev()
        self.assertEqual(round(stdev, 2), 2.52)
        
    def test_pmf(self):
        self.assertEqual(round(self.poisson.pmf(10), 2), 0.05)
    
    def test_cdf_single(self):
        self.assertEqual(round(self.poisson.cdf(7), 2), 0.69)
    
    def test_cdf_interval(self):
        self.assertEqual(round(self.poisson.cdf((8, 12)), 2), 0.29)

    def test_add(self):
        poisson_one = Poisson(2.5)
        poisson_two = Poisson(7.5)
        poisson_sum = poisson_one + poisson_two
        
        self.assertEqual(poisson_sum.m, 10)
    
if __name__ == '__main__':
    unittest.main()