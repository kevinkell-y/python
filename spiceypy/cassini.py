# Program Name: Cassini Position Example
# Programmer: Kevin Kelly
# Date: 09/16/2021
# Source: SpiceyPy Docs Project Example: https://spiceypy.readthedocs.io/en/v4.0.2/exampleone.html


# We will use SpiceyPy to plot the position of the Cassini spacecraft
# relative to the barycenter of Saturn
# (Barycenter is the center of mass of mass of two or more bodies that orbit one another)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# First import SpiceyPy and test it out
import spiceypy as spice

# Print out the toolkit version
spice.tkvrsn("TOOLKIT")

# The meta kernel file contains entries pointing to the following SPICE kernels, which the user needs to download.
#   https://naif.jpl.nasa.gov/pub/naif/generic_kernels/lsk/a_old_versions/naif0009.tls
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/sclk/cas00084.tsc
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/pck/cpck05Mar2004.tpc
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/fk/release.11/cas_v37.tf
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/ck/04135_04171pc_psiv2.bc
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/030201AP_SK_SM546_T45.bsp
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/ik/release.11/cas_iss_v09.ti
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/020514_SE_SAT105.bsp
#   https://naif.jpl.nasa.gov/pub/naif/CASSINI/kernels/spk/981005_PLTEPH-DE405S.bsp
#
#   The following is the contents of a metakernel that was saved with
#   the name 'cassMetaK.txt'.
#   \begindata
#   KERNELS_TO_LOAD=(
#   '~/naif/cassini-position-example/cassini-metakernels/naif0009.tls',
#   '~/naif/cassini-position-example/cassini-metakernels/cas00084.tsc',
#   '~/naif/cassini-position-example/cassini-metakernels/cpck05Mar2004.tpc',
#   '~/naif/cassini-position-example/cassini-metakernels/020514_SE_SAT105.bsp',
#   '~/naif/cassini-position-example/cassini-metakernels/981005_PLTEPH-DE405S.bsp',
#   '~/naif/cassini-position-example/cassini-metakernels/030201AP_SK_SM546_T45.bsp',
#   '~/naif/cassini-position-example/cassini-metakernels/04135_04171pc_psiv2.bc',
#   '~/naif/cassini-position-example/cassini-metakernels/cas_v37.tf',
#   '~/naif/cassini-position-example/cassini-metakernels/cas_iss_v09.ti')
#   \begintext
#

spice.furnsh("./cassiniMetaKernel.txt")

step = 4000

# We're going to get positions between these two dates
utc = ['Jun 20, 2004', 'Dec 1, 2005']

# Get et values one and two, we could vectorize str2et
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print("ET One: {}, ET Two: {}".format(etOne, etTwo))
