TotalDepth
==========

Petrophysical data processing and presentation

(C) Paul Ross: cpipdev@googlemail.com


Alpha Release 2012-03-03
========================

This is a pre-release of TotalDepth.


Requirements
------------
Python 3, Cython, and numpy.

Tested with:
Python 3.2
Cython 0.14.1
numpy 1.6.0.b2


Installation
------------
Unzip/chekout TotalDepth to any directory referred to here as <TOTALDEPTH>.

Put <TOTALDEPTH>/src on your PYTHONPATH

Some parts need to be built with Cython by hand:

cd <TOTALDEPTH>/src/TotalDepth/LIS/core
python3 setup.py build_ext --inplace


Testing the Installation
------------------------
cd <TOTALDEPTH>/src/TotalDepth/LIS/core
python3 test/UnitTests.py


Running Unit Tests
------------------
Navigate a command line to: TBD

Execute: python3 test/UnitTests.py


In this release
===============
TBD.

doc/
----
Some documentation and tutorials, fairly limited at the moment.

src/
----
Source code of TotalDepth.

DeTif.py - Reads a TIF delimited file and writes a version without TIF markers. 
DumpFrameSet.py - Reads a LIS file and writes out tab separated values of each frame.
Index.py - Reads LIS file or directory and indexes the LIS files. This can be used for pre-indexing or performance measurement.
LisToHtml.py - Generate HTML summary of each LIS file. Takes input/output directories/files.
PlotLogPasses.py - Generate SVG plots of each pass in as LIS file. Takes input/output directories/files.
ProcLisPath.py - Provides multiprocessing support for file and directory processing.
RandomFrameSetRead.py - Performance measurement of accessing LIS frame data.

