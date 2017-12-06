import weibull

import matplotlib.pyplot as plt

# 62 units run to 62 million time units
t = [6.2e7] * 62
ww = weibull.Weibayes(t, cl=95, beta=2)

# display plot and lifetime block
ww.display()

# annotate with B2 (98% survival) values
ww.plot_annotate(2)

plt.show()