# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt, seaborn as sns

def haseebs_random_sampling(values, sample_size, num_samples, with_replacement):
    """
    Perform random sampling on an array of values.

    Parameters:
        values (list or array-like): The input array of values
        sample_size (int): The size of each sample
        num_samples (int): The number of samples to generate
        with_replacement (bool): Whether sampling should be with or without replacement

    Returns:
        numpy array: A list of samples' means, where each sample is a randomly selected subset of the input values
        mean: The mean of the samples' means
        standard deviation: The standard deviation of the samples' means
        histogram of sample means: Plots a histogram of the samples' means
    """

    try:
        # Check if sample size is valid when sampling without replacement
        if not with_replacement and sample_size > len(values):
            raise ValueError("Sample size cannot exceed the number of values in the array when sampling without replacement.")

        # Generate samples
        sample_means = []
        for _ in range(num_samples):
            sample = np.random.choice(values, size=sample_size, replace=with_replacement)
            sample_means.append(sample.mean())

        # plot the histogram of sample means
        sns.histplot(sample_means, kde=True)
        plt.title('Histogram of Sample Means')
        plt.xlabel('Mean')
        plt.ylabel('Frequency')
        plt.show()

        return np.array(sample_means), np.mean(sample_means), np.std(sample_means)


    except ValueError as err:
        return str(err)
