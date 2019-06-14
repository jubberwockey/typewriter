# sympy rendering to png or dvi
import sympy as sp

x = sp.symbols('x')
eqn = sp.Integral(x**2,x)
latex_str = sp.latex(eqn)
latex_str

preamble = r"""\documentclass[preview,12pt]{standalone}
\usepackage{amsfonts}
\usepackage{amsmath}
\usepackage{amsfonts}
\begin{document}
"""
sp.preview(r'\['+latex_str+r'\]', euler=False, output='svg',
           # viewer='file',
           # filename='render_test.dvi',
           preamble=preamble,
           # packages=('amsfonts',),
           dvioptions=["-T", "tight", "-z", "0", "--truecolor", "-D 600", "-bg", "Transparent"],
           outputTexFile='render_test.tex')


# matplotlib renderer
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['text.usetex'] = True

latex_str = r'\begin{array}{cc}a&b\\c&d\end{array}'

plt.text(0, 0, '$'+latex_str+'$')
ax = plt.gca()
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
plt.show()
