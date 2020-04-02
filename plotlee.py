import matplotlib.pyplot as plt
import matplotlib.ticker as tick

"""
Helper library for doing matplotlib plots  Eventually move this to path
Lee prevost
"""


def scale(x, pos, format_spec=",1", scalar=None, precision= 1, currency=None):
    """Helper function for scaling figures

    x: tick value x
    pos: position (needed only for function to work)
    sig_figures = integer, 1 for decimal plus 1 sig figure.

    scalar:  string, options are "M" for millions, "B" for billions, or "K" for thousands or "" for no scale(default)

    currency: string, "$" or other currency figure.  default: None


    format_spec
    Optional. If omitted returns a string representation of an object. General form:
    [[fill]align][sign][#][0][width][,][.precision][type]

    https://python-reference.readthedocs.io/en/latest/docs/functions/format.html
    """
    
    scalar_dict = {"M": 1e-6,
            "K": 1e-3,
            "B": 1e-9,
            "T": 1e-12}

    scalar = scalar.upper()

    if currency:
        format_str = "{}{}".format(currency, format_str)
    if precision:
        format_str = "{}.{}".format(format_str, precision)
    x = int(x)*scalar_dict[scalar]
    format_spec = "{}{}{}".format(currency, format_spec, precision)
    s = format(x, ",")

    return '{0}{1}1.{2}{3}'.format(currency, s, sig_figures, format_str.upper())


def set_ticks(self, ax, axis = "x", sig_figures=None, format_str=None, currency=None,
                xmax=1, **formatterkwargs):
    """Helper function for setting major tick formats

        internal for function.   Override only if needed to supply
        x: tick value x
        pos: position (needed only for function to work)

        required:
        ax: matplotlib axis object
        axis: string, "x" for x-axis, "y" for y axis.  If both, run for each.
        sig_figures = integer, 1 for decimal plus 1 sig figure.

        format_str:  string, options are
            "M" for millions,
            "B" for billions, or
            "K" for thousands or
            "T" for trillions
            "%" for percent
            None for no format

        xmax: int, only used if format_str is %.  scalar for integer value.

        currency: string, "$" or other currency figure.  default: None
        """

    if self:
        ax = self
    if not isinstance(ax, plt.axes):
        raise TypeError("Expected matplotlib.axes object but got type: {}".format(type(ax)))

    if type (axis, sig_figures, format_str, currency) is not str:
        raise TypeError("{} expected to be of type string".format((axis, sig_figures, format_str, currency)))

    if format_str is ("M", "B", "K", "T"):
        formatter = tick.FuncFormatter(scale(format_spec=format_spec, ))

    if format_str is "%":
        formatter = tick.PercentFormatter(xmax=1, decimals= sig_figures, **formatterkwargs)


    if axis is "x":
        return ax.get_xaxis().set_major_formatter(formatter)

    if axis is "y":
        return ax.get_yaxis().set_major_formatter(formatter)



if __name__ == "main":

    y= [5, 10, 15, 20, 30]

    x = [10, 1000, 10000, 1e6, 1e9]

