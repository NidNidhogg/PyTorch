# -*- coding: utf-8 -*-
"""00_pytorch_fundamentals.ipynb

Automatically generated by Colaboratory.

"""

import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

scalar = torch.tensor(7)
scalar

"""**Introduction to Tensors**

Creating tensors

PyTorch tensors are created using 'torch.tensor()'

https://pytorch.org/docs/stable/tensors.html
"""

# scalar
scalar = torch.tensor(7)
scalar

scalar.ndim

#Get tensor back as Python int
scalar.item()

# Vector
vector = torch.tensor([7, 7])
vector

vector.ndim

vector.shape

# MATRIX
MATRIX = torch.tensor([[7, 8],
                       [9,10]])
MATRIX

MATRIX.ndim

MATRIX[1]

MATRIX.shape

# TENSOR
TENSOR = torch.tensor([[[[1, 2, 3],
                        [3, 7, 12],
                        [2,4,5],
                        [34,56,10]]]])
TENSOR

TENSOR.ndim

TENSOR.shape

"""**Random tensors**

Why random tensors?

Random tensors are important because the way many neural networks learn is that they start with tensors full of random numbers and then adjust those random numbers to better represent the data.

`Start with random numbers -> look at data -> update randon numbers -> look at data  -> update random numbers`

Torch random tensors  https://pytorch.org/docs/stable/generated/torch.rand.html
"""

# Create a random tensor of size (3, 4)
random_tensor = torch.rand(3, 4)
random_tensor

# Create a random tensor with similar shape to an image tensor
random_image_size_tensor = torch.rand(size=(224, 224, 3)) #height, width, colour channel (R, G, B)
random_image_size_tensor.shape, random_image_size_tensor.ndim

"""**Zeros and ones**"""

## Create a tensor of all zeros
zeros = torch.zeros(size=(3,4))
zeros

zeros*random_tensor

# Create a tensor of all ones
ones = torch.ones(size=(3,4))
ones

ones.dtype

ones*random_tensor

"""**Creating a range of tensore and tensors-like**

"""

# Use torch.range() and get deprecated message use torch.arrange()
torch.arange(1,11)

one = torch.arange(start=0, end=1000, step=78)
one

# Create a tensor-like
two = torch.zeros_like(input=one)
two

"""**Tensor datatypes**

**Note** Tensor datatypes is one of the three big errors you'll run into  with PyTorch & deep learning

1. Tensors not right datatype
2. Tensors not right shape
3. Tensors not on the right device

Precision in computer science
https://en.wikipedia.org/wiki/Precision_(computer_science)
"""

# Float 32 tensor
float_32_tensor = torch.tensor([3.0, 6.0, 9.0],
                               dtype=None, # What datatype is the tensor (float32 or float16)
                               device=None, # What device is your tensor on
                               requires_grad=False) #whether or not to track gradience with this tensor operations
float_32_tensor

float_32_tensor.dtype

float_16_tensor = float_32_tensor.type(torch.float16)
float_16_tensor

float_16_tensor * float_32_tensor



"""**Getting information from tensors** (tensors attrbutes)

1. Tensors not right datatype - to get datatype from a tensor, can use `tensor. dtype`
2. Tensors not right shape - to get shape from a tensor, can use `tensor.shape`
3. Tensors not on the right device - to get device from a tensor, can use `tensor.device`
"""

# Create a tensor
some_tensor = torch.rand(3, 4)
some_tensor

# Find out detailes about some_tensor
print(some_tensor)
print(f"Datatype of tensor: {some_tensor.dtype}")
print(f"Shape of tensor: {some_tensor.shape}")  #tensor.size do the same as tensor.shape {tensor.size is a function}
print(f"Device tensor is on: {some_tensor.device}")

"""Manupulating Tensors (tensor operations)

Tensor operations include:

*Addition

*Subtraction

*Multiplication (element-wise)

*Division

*Matrix multiplication https://www.mathsisfun.com/algebra/matrix-multiplying.html
"""

# Create a tensor and add 10 to it
tensor = torch.tensor([1,2,3])
tensor +10

#Multiply tensor by ten
tensor * 10

tensor

# Substract 10
tensor - 10

# Try out Pytorch in-built functions
torch.mul(tensor, 10)

torch.add(tensor, 10)

"""**Matrix multiplication**

Two main ways of performing multiplication in neural networks and deep learning:
1. Element-wise multiplication
2. Matrix multiplication (dot product) https://en.wikipedia.org/wiki/Dot_product

More info about multiplying  matrices https://www.mathsisfun.com/algebra/matrix-multiplying.html

There are two main rules that performing matrix multiplication needs to satisfy

1. The **inner dimensions** must match:
* ~(3,2) @ (3, 2) won't work
* ~(2, 3) @ (3,2) will work
* ~(3, 2) @ (2, 3) will work

2. The resulting matrix has the shape of the **outer dimensions**:
*~(2,3) @ (3,2) -> ~(2,2)`

*~(2,3) @ (3,2) -> ~(3,3)`

"""

torch.matmul(torch.rand(3,2), torch.rand(2, 3))

# Element wise multiplication
print(tensor, "*", tensor)
print(f"Equals: {tensor * tensor}")

# Matrix multiplictaion
torch.matmul(tensor, tensor)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# value = 0
# for i in range(len(tensor)):
#   value += tensor[i] * tensor[i]
# print(value)

# Commented out IPython magic to ensure Python compatibility.
# %%time
# torch.matmul(tensor, tensor)

"""One of the most common errors in deep learning: shape errors

http://matrixmultiplication.xyz/

"""

# Shapes for matrix multiplication
tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5,6]])
tensor_B = torch.tensor([[7, 10],
                         [8, 11],
                         [9, 12]])
torch.matmul(tensor_A, tensor_B) # or torch.mm instead of torch.matmul (it's for writing less code)

tensor_A.shape, tensor_B.shape

"""To fix our tensor shape issues, we can manipulate the shape of one of our tensors using a **transpose**.

A **transpose** switches the axes or dimensions of a given tensor.
"""

tensor_B.T, tensor_B.T.shape

tensor_B, tensor_B.shape

# The matrix multiplication operation works when tensor_B is transposed
print(f"Original shapes: tensor_A = {tensor_A.shape}, tensor_B = {tensor_B.shape}")
print(f"New shapes: tensor_A = {tensor_A.shape} (same shape as above), tensor_B.T = {tensor_B.T.shape}")
print(f"Multiplying: {tensor_A.shape} @ {tensor_B.T.shape} <- inner dimensions must match")
print("Output:\n")
output = torch.matmul(tensor_A, tensor_B.T)
print(output)
print(f"\nOutput shape: {output.shape}")

"""**Finding the min, max, mean, sum, etc(tensor aggregation)**"""

# Create a tensor
x = torch.arange(1, 100, 10)
x

# Find the min
torch.min(x), x.min()

# Find the max
torch.max(x), x.max()

#Find the mean - note: the torch.mean() function reqires a tensor of float32 datatype to work
torch.mean(x.type(torch.float32)), x.type(torch.float32).mean()

# Find the sum
torch.sum(x), x.sum()

"""**Find the poitional min and max**"""

x

# Find the position in tensor that has the minimum value with argmin() -> returns index position of target tensor where the minimum value occurs
x.argmin(), x.argmax()

x[0], x[9]

x

"""**Reshaping, stacking, squeezing and unsqeezing tensors**

* Reshaping - reshapes an input tensor to a defined shaped

* View - return a view of an input tensor of certain shape but keep the same memory as the original tensor

* Stacking - combine mltiple tensors on top of each other (vstack - vertical stack) or side by side (hstack - horizontal stack)
* Squeeze - removes all `1` dimensions from a tensor

* Unsqueeze - add a `1` dimension to a target tensor

* Permute - return a view of the input with dimensions permuted (swapped) in a certain way.
"""

import torch
x = torch.arange(1., 10.)
x, x.shape

# Add an extra dimension
x_reshaped = x.reshape(1, 9)
x_reshaped, x_reshaped.shape

# Change the view
z = x.view(1, 9)
z, z.shape

# Chahging z changes x (because a view of a tensor shares the same memory as the original input)
z[:, 0] = 5
z, x

# Stack tensors on top of each other
x_stacked = torch.stack([x, x, x, x], dim = 0)
x_stacked

# torch.squeeze() - removes all single dimensions from a target tensor
print(f"Previous tensor: {x_reshaped}")
print(f"Previous shape: {x_reshaped.shape}")

#Remove extra dimensions from x_reshaped
x_squeezed = x_reshaped.squeeze()
print(f"\nNew tensor: {x_squeezed}")
print(f"\nNew shape: {x_squeezed.shape}")

# torch.unsqueeze() - adds a single dimension to a target tensor at a specific dim (dimension)
print(f"Previous target: {x_squeezed}")
print(f"Previous shape: {x_squeezed.shape}")

# Add an extra dimension  with unsqeeze
x_unsqueezed = x_squeezed.unsqueeze(dim=0)
print(f"\nNew tensor: {x_unsqueezed}")
print(f"\nNew shape: {x_unsqueezed.shape}")

# torche.permute - rearranges the dimensions of a target tensor in a specified order
x_original = torch.rand(size=(224, 224, 3)) # [height, weight, colour_channels]

# Permute the original tensor to rearrange the axis (or dim) order
x_permuted = x_original.permute(2,0,1) #shift axis 0->1, 1->2, 2->0
x_permuted.shape # [colour_channels, height, weight]

x_original[0, 0, 0] = 378623
x_original[0, 0, 0], x_permuted[0, 0, 0]

"""**Indexing (selecting data from tensors)**

Indexing with Pytorch is similar to indexing with NumPy.
"""

# Create a tensor
import torch
x = torch.arange(1, 10).reshape(1, 3, 3)
x, x.shape

# Let's index on our new tensor
x[0]

# Let's index on the middle bracket (dim=1)
x[0][0]

# Let's index on the most inner bracket (last dimension)

x[0][2][2]

# You can also use ":" to select "all" of a target dimension
x[:, 0]

# Get all values of 0th and 1st dimensions but only index 1 of second dimension
x[:, :, 1]

# Get all values of the 0 dimension but only the 1st index value of 1st and 2nd dimensions
x[0, 1, 1]

# Get index 0  of 0th and 1st dimensions and all values of 2nd dimension
x[0, 0, :]

#Index on x to return 9
x[0][2][2]

#Index on x to return 3,6,
x[:, :, 2]

"""**PyTorch tensors and NumPy**

Numpy is a popular scientific Python numerical computing library.

And because of this, PyTorch has functionality to interact this it.

* Data in NumPy, want in PyTorch tensor -> `torch.from_numpy(ndarray)`
* PyTorch tensor -> NumPy `torch.Tensor.numpy()`
"""

# NumPy array to tensor
import torch
import numpy as np

array = np.arange(1.0, 8.0)
tensor = torch.from_numpy(array) #warning when converting from numpy -> pytorch, pytorch reflects numpy's default datatype of float64 unless specified otherwise
array, tensor

# Change the value of array
array = array + 1
array, tensor

# Tensor to NumPy array
tensor = torch.ones(7)
numpy_tensor = tensor.numpy()
tensor, numpy_tensor

# Change the tensor, what happens to 'numpy_tensor'
tensor = tensor + 1
tensor, numpy_tensor

"""**Reproducibility (trying to take random out of random)**

In short how a neural network learns:
`start with random numbers -> tensor operations -> update random numbers to try and make them better representations of the data -> again -> again -> again...`

To reduce the randomness in neural networks and PyTorch  comes the concept of a **random seed**.

What the random seed does is "flavour" the randomness.

https://pytorch.org/docs/stable/notes/randomness.html

https://en.wikipedia.org/wiki/Random_seed
"""

import torch

# Create two random tensors
random_tensor_A = torch.rand(3, 4)
random_tensor_B = torch.rand(3, 4)

print(random_tensor_A)
print(random_tensor_B)
print(random_tensor_A == random_tensor_B)

# Let's make some random but reproducible tensors

import torch

# Set the random seed
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
random_tensor_C = torch.rand(3, 4)

torch.manual_seed(RANDOM_SEED)
random_tensor_D = torch.rand(3, 4)

print(random_tensor_C)
print(random_tensor_D)
print(random_tensor_C == random_tensor_D)

"""**Running tensors and PyTorch objects on the GPUs (and making faster computations)**

GPUs = faster computation on numbers, thanks to CUDA + NVIDIA hardware + PyTorch working behind the scenes to make everything good.

### 1. Getting a GPU

1.Easiest - Use Google colab for a free GPU

2.Use your own GPU - take a little bit of setup and requires the investment of purchasing a GPU.

3.Cloud computing

"""

!nvidia-smi

# Check for GPU access with PyTorch
import torch
torch.cuda.is_available()

# Setup device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"
device

# Count number of devices
torch.cuda.device_count()

"""**2. Putting tensors (and models) on GPU**

The reason we want our tensors/models on GPU is because using of GPU results in faster computation.
"""

# Create a tensor (default on the CPU)
tensor = torch.tensor([1, 2, 3])

#Tensor not on the GPU
print(tensor, tensor.device)

# move tensor to GPU (if available)
tensor_on_gpu = tensor.to(device)
tensor_on_gpu

"""**3. Moving tensors back to the CPU**"""

# If a tensor is on GPU, can't transform it to NumPy
tensor_on_gpu.numpy()

# To fix the GPU tensor with NumPy, we can first set it to the CPU
tensor_back_on_cpu = tensor_on_gpu.cpu().numpy()
tensor_back_on_cpu

tensor_on_gpu
