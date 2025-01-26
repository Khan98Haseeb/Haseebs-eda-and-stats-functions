from setuptools import setup, find_packages

setup(
    name='haseebs-eda-and-stats-functions',  # Replace with your package name
    version='0.1.0',
    description='A collection of EDA and statistics functions by Haseeb',
    author='Haseeb Khan',
    author_email='haseeb.dataanalytics@gmail.com',
    url='https://github.com/Khan98Haseeb/haseebs-eda-and-stats-functions',
    packages=find_packages(),  # Automatically finds Python packages in your repo
    install_requires=[
        'numpy',       # Dependency for numerical operations
        'pandas',      # Dependency for data manipulation
        'matplotlib',  # Dependency for plotting
        'seaborn'      # Dependency for advanced visualizations
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
