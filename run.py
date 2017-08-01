import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "flmodel"))

from flmodel.model import FuzzyLogicModel


FuzzyLogicModel.show_graphs()