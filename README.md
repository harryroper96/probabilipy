# ProbabiliPy

ProbabiliPy is a Python library for analysing probability distributions.

Users can read data from .txt files to instances of the Gaussian, Binomial and Poisson distribution models. The package can be used to:

1. Calculate the properties of a distribution, such as the mean and standard deviation
2. Plot a distribution visually
3. Calculate a distribution's probability mass and cumulative density functions for given values and intervals

### Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Contributing](#contributing)
4. [License](#license)

## Installation <a name="installation"></a>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ProbabiliPy.

```bash
pip install probabilipy
```

### Dependencies

The package should run with no issues using Python version 3.

To run the package, users also need to have the following packages installed:

- [python-math](https://pypi.org/project/python-math/)
- [matplotlib](https://pypi.org/project/matplotlib/)
- [unittest](https://pypi.org/project/unittest/) (only required if using the test.py file)

## Usage <a name="usage"></a>

```python
import probabilipy

binomial = probabilipy.Binomial(p=0.5, n=10) # creates a binomial instance
binomial.mean # returns 5.0
binomial.stdev # returns 1.5811388300841898
binomial.plot_dist() # returns a histogram of the distribution
binomial.pmf(7) # returns 0.1171875
binomial.cdf((4, 8)) # returns 0.8173828125

```

## Contributing <a name="contributing"></a>
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License <a name="lecense"></a>
[MIT](https://choosealicense.com/licenses/mit/)
