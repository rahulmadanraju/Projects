# MNIST-Recognition-using-Keras-and-TensorFlow

The implementation and recognition of Modified National Institute of Standards and Technology database using the methodologies of Deep Learning with the help of libraries such as TensorFLow and Keras

# TensorFlow
TensorFlow is a free and open-source software library for dataflow and differentiable programming across a range of tasks. It is a symbolic math library, and is also used for machine learning applications such as neural networks.

### Installation
To install the current release for CPU-only:
```
pip install tensorflow
```
Use the GPU package for CUDA-enabled GPU cards:
```
pip install tensorflow-gpu
```

# Keras

Keras is a high-level neural networks API, written in Python and capable of running on top of [TensorFlow](https://github.com/tensorflow/tensorflow), [CNTK](https://github.com/Microsoft/cntk), or [Theano](https://github.com/Theano/Theano). It was developed with a focus on enabling fast experimentation. *Being able to go from idea to result with the least possible delay is key to doing good research.*

Use Keras if you need a deep learning library that:

- Allows for easy and fast prototyping (through user friendliness, modularity, and extensibility).
- Supports both convolutional networks and recurrent networks, as well as combinations of the two.
- Runs seamlessly on CPU and GPU.

Read the documentation at [Keras.io](https://keras.io).

Keras is compatible with: __Python 2.7-3.6__.

### Installation

Before installing Keras, please install one of its backend engines: TensorFlow, Theano, or CNTK. We recommend the TensorFlow backend.

- [TensorFlow installation instructions](https://www.tensorflow.org/install/).
- [Theano installation instructions](http://deeplearning.net/software/theano/install.html#install).
- [CNTK installation instructions](https://docs.microsoft.com/en-us/cognitive-toolkit/setup-cntk-on-your-machine).

You may also consider installing the following **optional dependencies**:

- [cuDNN](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/) (recommended if you plan on running Keras on GPU).
- HDF5 and [h5py](http://docs.h5py.org/en/latest/build.html) (required if you plan on saving Keras models to disk).
- [graphviz](https://graphviz.gitlab.io/download/) and [pydot](https://github.com/erocarrera/pydot) (used by [visualization utilities](https://keras.io/visualization/) to plot model graphs).

Then, you can install Keras itself. There are two ways to install Keras:

- **Install Keras from PyPI (recommended):**

Note: These installation steps assume that you are on a Linux or Mac environment.
If you are on Windows, you will need to remove `sudo` to run the commands below.

```sh
sudo pip install keras
```

If you are using a virtualenv, you may want to avoid using sudo:

```sh
pip install keras
```

- **Alternatively: install Keras from the GitHub source:**

First, clone Keras using `git`:

```sh
git clone https://github.com/keras-team/keras.git
```

 Then, `cd` to the Keras folder and run the install command:
```sh
cd keras
sudo python setup.py install
```

