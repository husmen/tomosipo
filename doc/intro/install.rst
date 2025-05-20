Install tomosipo
================

A minimal installation requires Python >= 3.11, CUDA 12.4 and a few packages
that are installed automatically with ``pip``:

* ``astra-toolbox==2.3.1``
* ``numpy>=2.2``
* ``torch==2.6``
* ``pytorch-lightning==2.5``

Installation using anaconda
---------------------------

Create a new environment (replace `X.X` by your CUDA version) and install
`tomosipo` using `pip`:

.. code-block:: bash

   conda create -n tomosipo python=3.11 cudatoolkit=<X.X>
   conda activate tomosipo
   pip install tomosipo


Install the latest development branch
-------------------------------------

To install the latest development branch from GitHub, first create a new
environment with Python 3.11 and CUDA:

.. code-block:: bash

    conda create -n tomosipo python=3.11 cudatoolkit=X.X

Then activate the environment and install tomosipo using pip:

.. code-block:: bash

    source activate tomosipo
    pip install git+https://github.com/ahendriksen/tomosipo@develop

Install optional dependencies
-----------------------------

To use tomosipo with PyTorch, QT, ODL, and CuPy, install them using ``pip``:

.. code-block:: bash

    pip install torch==2.6 pytorch-lightning==2.5 cupy pyqtgraph pyqt pyopengl
    pip install git+https://github.com/odlgroup/odl


.. _intro_install_with_pytorch:


Install with PyTorch
--------------------

To just install PyTorch support run

.. code-block:: bash

   pip install torch==2.6 pytorch-lightning==2.5

