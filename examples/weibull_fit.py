import weibull
import matplotlib.pyplot as plt

# create table of failure times at test initialization
units_in_test = 9
fail_times = [None] * units_in_test  # when test is started, there are no failure times

fail_times[8] = 6677
fail_times[0] = 8329
fail_times[1] = 8545

analysis = weibull.Weibull(fail_times)
analysis.fit()

analysis.plot(susp=1)
analysis.plot_fits('yx', linestyle='--')

plt.show()  # todo: make this unnecessary